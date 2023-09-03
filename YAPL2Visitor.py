# Generated from YAPL2.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPL2Parser import YAPL2Parser
else:
    from YAPL2Parser import YAPL2Parser

# This class defines a complete generic visitor for a parse tree produced by YAPL2Parser.
from table.attribute_table import *
from table.types_table import *
from table.class_table import *
from table.function_table import *
from errors import semanticError


class YAPL2Visitor(ParseTreeVisitor):
    
    def __init__(self, classTable, functionTable, attributeTable, typesTable, foundErrors):
        super().__init__()
        self.functionTable = functionTable
        self.attributeTable = attributeTable
        self.typesTable = typesTable
        self.classTable = classTable
        self.currentMethod = None
        self.currentScope = 1
        self.currentClass = "Debugg"
        self.currentMethodId = 10
        self.foundErrors = []
    
    def findFamily(self, currentClass, wantedClass):
        dad = self.classTable.findEntry(currentClass.inherits)
        family = []
        while dad:
            family.append(dad.name)
            dad = self.classTable.findEntry(dad.inherits)
        print(family)
        if wantedClass not in family:
            return False
        else:
            return True

    # Visit a parse tree produced by YAPL2Parser#program.
    def visitProgram(self, ctx:YAPL2Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#programBlock.
    def visitProgramBlock(self, ctx:YAPL2Parser.ProgramBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#classDEF.
    def visitClassDEF(self, ctx:YAPL2Parser.ClassDEFContext):
        className = str(ctx.TYPEID()[0])
        if len(ctx.TYPEID()) > 1:
            parentClass = str(ctx.TYPEID()[1])
            if not self.classTable.findEntry(parentClass):
                error = semanticError(ctx.start.line, "Class " + parentClass + " not defined")
                self.foundErrors.append(error)
                return "Error"
        else:
            parentClass = None
        # if parentClass:
        #     entry = ClassTableEntry(className, parentClass)
        # else:
        #     entry = ClassTableEntry(className)
        # self.classTable.addEntry(entry)
        self.currentClass = className
        self.currentMethod = None
        self.currentScope = 1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#MethodDef.
    def visitMethodDef(self, ctx:YAPL2Parser.MethodDefContext):
        self.currentMethodId += 1
        functionName = str(ctx.OBJECTID())
        type = str(ctx.TYPEID())
        # entry = FunctionTableEntry(self.currentMethodId,functionName, type, self.currentScope, self.currentClass)
        # self.functionTable.addEntry(entry)
        if type == "SELF_TYPE":
            type = self.currentClass
        self.currentMethod = functionName
        self.currentScope = 2
        for node in ctx.formal():
            self.visit(node)
        childrenResult = self.visit(ctx.expr())
        if childrenResult == "SELF_TYPE":
            childrenResult = self.currentClass
    
        if childrenResult == type or self.findFamily(self.classTable.findEntry(childrenResult), type):
            return type
        else:
            error = semanticError(ctx.start.line, "Function " + functionName + " returns " + childrenResult + " instead of " + type)
            self.foundErrors.append(error)
            return "Error"

    # Visit a parse tree produced by YAPL2Parser#FeactureDecalration.
    def visitFeactureDecalration(self, ctx:YAPL2Parser.FeactureDecalrationContext):
        # featureName = str(ctx.OBJECTID())
        # featureType = str(ctx.TYPEID())
        # if self.currentMethod:
        #     entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, self.currentMethodId)
        # else:
        #     entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, None)
        # self.attributeTable.addEntry(entry)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#formal.
    def visitFormal(self, ctx:YAPL2Parser.FormalContext):
        # featureName = str(ctx.OBJECTID())
        # featureType = str(ctx.TYPEID())
        # entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, self.currentMethodId, True)
        # self.attributeTable.addEntry(entry)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#newExpr.
    def visitNewExpr(self, ctx:YAPL2Parser.NewExprContext):
        classType = str(ctx.TYPEID())
        if self.classTable.findEntry(classType):
            return classType
        else:
            if self.typesTable.findEntry(classType):
                return classType
            else:
                error = semanticError(ctx.start.line, "Class " + classType + " not defined")
                self.foundErrors.append(error)
                return "Error"


    # Visit a parse tree produced by YAPL2Parser#divideExpr.
    def visitDivideExpr(self, ctx:YAPL2Parser.DivideExprContext):
        childrenResults = []
        for node in ctx.expr():
            childresult = self.visit(node)
            childrenResults.append(childresult)

        if childrenResults[0] == "Int" and childrenResults[-1] == "Int":
            return "Int"
        else:
            error = semanticError(ctx.start.line, "Cannot divide " + childrenResults[0] + " and " + childrenResults[-1])
            self.foundErrors.append(error)
            return "Error"


    # Visit a parse tree produced by YAPL2Parser#FunctionExpr.
    def visitFunctionExpr(self, ctx:YAPL2Parser.FunctionExprContext):
        childrenResults = []
        for node in ctx.expr():
            childresult = self.visit(node)
            if childresult == "SELF_TYPE":
                childresult = self.currentClass
            childrenResults.append(childresult)
        #Check if the function is defined
        methodEntry = self.functionTable.findEntryByName(str(ctx.OBJECTID()), self.currentClass)
        if methodEntry:
            #Check if the number of arguments is correct
            savedParams = self.attributeTable.findParamsOfFunction(methodEntry.id)
            if len(childrenResults) != len(savedParams):
                error = semanticError(ctx.start.line, "Function " + methodEntry.name + " expects " + str(len(savedParams)) + " parameters but " + str(len(savedParams)) + " were given")
                self.foundErrors.append(error)
                return "Error"
            #Check if the types of the arguments are correct
            for i in range(len(childrenResults)):
                if childrenResults[i] != savedParams[i].type:
                    error = semanticError(ctx.start.line, "Function " + methodEntry.name + " expects " + savedParams[i].type + " as parameter " + str(i+1) + " but " + childrenResults[i] + " was given")
                    self.foundErrors.append(error)
                    return "Error"
            if methodEntry.type == "SELF_TYPE":
                return childrenResults[0]
            else:
                return methodEntry.type
        #Else check if the function belongs to a parent class
        else:
            usingClass = self.classTable.findEntry(self.currentClass)
            if usingClass:
                parrentClass = usingClass.inherits
                if parrentClass:
                    methodEntry = self.functionTable.findEntryByName(str(ctx.OBJECTID()), parrentClass)
                    if methodEntry:
                        #Check if the number of arguments is correct
                        savedParams = self.attributeTable.findParamsOfFunction(methodEntry.id)
                        if len(childrenResults) != len(savedParams):
                            error = semanticError(ctx.start.line, "Function " + methodEntry.name + " expects " + str(len(savedParams)) + " parameters but " + str(len(savedParams)) + " were given")
                            self.foundErrors.append(error)
                            return "Error"
                        #Check if the types of the arguments are correct
                        for i in range(len(childrenResults)):
                            if childrenResults[i] != savedParams[i].type:
                                error = semanticError(ctx.start.line, "Function " + methodEntry.name + " expects " + savedParams[i].type + " as parameter " + str(i+1) + " but " + childrenResults[i] + " was given")
                                self.foundErrors.append(error)
                                return "Error"
                        if methodEntry.type == "SELF_TYPE":
                            return childrenResults[0]
                        else:
                            return methodEntry.type
                    else:
                        error = semanticError(ctx.start.line, "Function " + str(ctx.OBJECTID()) + " not defined")
                        self.foundErrors.append(error)
                        return "Error"
                else:
                    error = semanticError(ctx.start.line, "Function " + str(ctx.OBJECTID()) + " not defined")
                    self.foundErrors.append(error)
                    return "Error"
            else:
                return "Error"


    # Visit a parse tree produced by YAPL2Parser#integerExpr.
    def visitIntegerExpr(self, ctx:YAPL2Parser.IntegerExprContext):
        return "Int"


    # Visit a parse tree produced by YAPL2Parser#trueExpr.
    def visitTrueExpr(self, ctx:YAPL2Parser.TrueExprContext):
        return "Bool"


    # Visit a parse tree produced by YAPL2Parser#MethodExpr.
    def visitMethodExpr(self, ctx:YAPL2Parser.MethodExprContext):
        childrenResults = []
        for node in ctx.expr():
            childresult = self.visit(node)
            if childresult == "SELF_TYPE":
                childresult = self.currentClass
            childrenResults.append(childresult)
        mainClass = childrenResults[0]
        #Check if we are using a method from a parent class
        if ctx.TYPEID():
            parentClass = str(ctx.TYPEID())
            #Check if the parent class is defined
            if not self.classTable.findEntry(parentClass):
                error = semanticError(ctx.start.line, "Class " + parentClass + " not defined")
                self.foundErrors.append(error)
                return "Error"
            currentClass = self.classTable.findEntry(mainClass)
            if currentClass.inherits != parentClass:
                dad = self.classTable.findEntry(currentClass.inherits)
                family = []
                while dad:
                    family.append(dad.name)
                    dad = self.classTable.findEntry(dad.inherits)         
                if parentClass not in family:
                    error = semanticError(ctx.start.line, "Class " + mainClass + " can't acces methods from class " + parentClass)
                    self.foundErrors.append(error)
                    return "Error"

            # Check if the method is defined in the parent class
            methodEntry =  self.functionTable.findEntryByName(str(ctx.OBJECTID()), parentClass)
            if methodEntry:
                params = childrenResults[1:]
                savedParams = self.attributeTable.findParamsOfFunction(methodEntry.id)
                if len(params) != len(savedParams):
                    error = semanticError(ctx.start.line, "Function " + methodEntry.name + " expects " + str(len(savedParams)) + " parameters but " + str(len(params)) + " were given")
                    self.foundErrors.append(error)
                    return "Error"
                for i in range(len(params)):
                    if params[i] != savedParams[i].type:
                        error = semanticError(ctx.start.line, "Function " + methodEntry.name + " expects " + savedParams[i].type + " as parameter " + str(i+1) + " but " + params[i] + " was given")
                        self.foundErrors.append(error)
                        return "Error"
                if methodEntry.type == "SELF_TYPE":
                    return childrenResults[0]
                else:
                    return methodEntry.type
            else:
                error = semanticError(ctx.start.line, "Method " + str(ctx.OBJECTID()) + " not defined in " + parentClass)
                self.foundErrors.append(error)
                return "Error"
        else:
            # Check if the method is defined in the current class
            methodEntry = self.functionTable.findEntryByName(str(ctx.OBJECTID()), mainClass)
            if methodEntry:
                params = childrenResults[1:]
                savedParams = self.attributeTable.findParamsOfFunction(methodEntry.id)
                if len(params) != len(savedParams):
                    error = semanticError(ctx.start.line, "Function " + methodEntry.name + " expects " + str(len(savedParams)) + " parameters but " + str(len(params)) + " were given")
                    self.foundErrors.append(error)
                    return "Error"
                for i in range(len(params)):
                    if params[i] != savedParams[i].type:
                        error = semanticError(ctx.start.line, "Function " + methodEntry.name + " expects " + savedParams[i].type + " as parameter " + str(i+1) + " but " + params[i] + " was given")
                        self.foundErrors.append(error)
                        return "Error"
                if methodEntry.type == "SELF_TYPE":
                    return childrenResults[0]
                else:
                    return methodEntry.type
            else:
                error = semanticError(ctx.start.line, "Method " + str(ctx.OBJECTID()) + " not defined in " + mainClass)
                self.foundErrors.append(error)
                return "Error"

    # Visit a parse tree produced by YAPL2Parser#DeclarationExpression.
    def visitDeclarationExpression(self, ctx:YAPL2Parser.DeclarationExpressionContext):
        leftside = str(ctx.OBJECTID())
        #search for leftside in attribute table
        leftsideEntry = self.attributeTable.findEntry(leftside, self.currentClass, self.currentMethodId,self.currentScope)
        #if not found, search without methdod
        if leftsideEntry is None:
            leftsideEntry = self.attributeTable.findEntry(leftside, self.currentClass, None,self.currentScope - 1)
        if leftsideEntry is None:
            error = semanticError(ctx.start.line, "Variable " + leftside + " not defined")
            self.foundErrors.append(error)
            return "Error"
        childrenResult = self.visitChildren(ctx)
        if childrenResult == leftsideEntry.type or self.findFamily(self.classTable.findEntry(childrenResult), leftsideEntry.type):
            return leftsideEntry.type
        else:
            error = semanticError(ctx.start.line, "Can't assign " + childrenResult + " to " + leftsideEntry.type)
            self.foundErrors.append(error)
            return "Error"
        
    # Visit a parse tree produced by YAPL2Parser#ifElseExpr.
    def visitIfElseExpr(self, ctx:YAPL2Parser.IfElseExprContext):
        childrenResults = []
        for node in ctx.expr():
            childrenResults.append(self.visit(node))
        #TODO Ask about the type of the condition
        if childrenResults[0] == "Bool":
            if childrenResults[1] == childrenResults[2]:
                return childrenResults[1]
            return "Object"
        else:
            error = semanticError(ctx.start.line, "If conditional must be boolean not " + childrenResults[0])
            self.foundErrors.append(error)
            return "Error"

    # Visit a parse tree produced by YAPL2Parser#lessExpr.
    def visitLessExpr(self, ctx:YAPL2Parser.LessExprContext):
        childrenResults = []
        for node in ctx.expr():
            childrenResults.append(self.visit(node))
        if childrenResults[0] == "Int" and childrenResults[1] == "Int":
            return "Bool"
        else:
            error = semanticError(ctx.start.line, "Cannot compare " + childrenResults[0] + " and " + childrenResults[1])
            self.foundErrors.append(error)
            return "Error"


    # Visit a parse tree produced by YAPL2Parser#BraketedExpr.
    def visitBraketedExpr(self, ctx:YAPL2Parser.BraketedExprContext):
        childrenResults = []
        for node in ctx.expr():
            childrenResults.append(self.visit(node))
        
        return childrenResults[-1]


    # Visit a parse tree produced by YAPL2Parser#multiplyExpr.
    def visitMultiplyExpr(self, ctx:YAPL2Parser.MultiplyExprContext):
        childrenResults = []
        for node in ctx.expr():
            childresult = self.visit(node)
            childrenResults.append(childresult)

        if childrenResults[0] == "Int" and childrenResults[-1] == "Int":
            return "Int"
        else:
            error = semanticError(ctx.start.line, "Cannot multiply " + childrenResults[0] + " and " + childrenResults[-1])
            self.foundErrors.append(error)
            return "Error"


    # Visit a parse tree produced by YAPL2Parser#letExpr.
    def visitLetExpr(self, ctx:YAPL2Parser.LetExprContext):
        self.currentScope = 3
        firstVisits = ctx.expr()[0:-1]
        firstVisitsResults = []
        for node in firstVisits:
            firstVisitsResults.append(self.visit(node))
        for i in range(len(ctx.OBJECTID())):
            newVarName = str(ctx.OBJECTID()[i])
            newVarType = str(ctx.TYPEID()[i])
            # newVarEntry = AttributeTableEntry(newVarName, newVarType, self.currentScope, self.currentClass, self.currentMethodId)
            # self.attributeTable.addEntry(newVarEntry)
            if i < len(firstVisitsResults):
                if firstVisitsResults[i] != newVarType:
                    error = semanticError(ctx.start.line, "Can't assign " + firstVisitsResults[i] + " to " + newVarType)
                    self.foundErrors.append(error)
                    return "Error"
        lastExpresionResult = self.visit(ctx.expr()[-1])
        return lastExpresionResult



    # Visit a parse tree produced by YAPL2Parser#stringExpr.
    def visitStringExpr(self, ctx:YAPL2Parser.StringExprContext):
        return "String"


    # Visit a parse tree produced by YAPL2Parser#lessEqualExpr.
    def visitLessEqualExpr(self, ctx:YAPL2Parser.LessEqualExprContext):
        childrenResults = []
        for node in ctx.expr():
            childrenResults.append(self.visit(node))
        if childrenResults[0] == "Int" and childrenResults[1] == "Int":
            return "Bool"
        else:
            error = semanticError(ctx.start.line, "Cannot compare " + childrenResults[0] + " and " + childrenResults[1])
            self.foundErrors.append(error)
            return "Error"
    


    # Visit a parse tree produced by YAPL2Parser#notExpr.
    def visitNotExpr(self, ctx:YAPL2Parser.NotExprContext):
        childrenResult = self.visit(ctx.expr())
        if childrenResult == "Bool" or childrenResult == "Int":
            return childrenResult
        else:
            error = semanticError(ctx.start.line, "Cannot use NOT operator on  " + childrenResult)
            self.foundErrors.append(error)
            return "Error"

    # Visit a parse tree produced by YAPL2Parser#whileExpr.
    def visitWhileExpr(self, ctx:YAPL2Parser.WhileExprContext):
        childrenResult = []
        for node in ctx.expr():
            childrenResult.append(self.visit(node))
        if childrenResult[0] == "Bool":
            return "Object"
        else:
            error = semanticError(ctx.start.line, "Cannot use " + childrenResult[0] + " as condition")
            self.foundErrors.append(error)
            return "Error"

    # Visit a parse tree produced by YAPL2Parser#addExpr.
    def visitAddExpr(self, ctx:YAPL2Parser.AddExprContext):
        childrenResults = []
        for node in ctx.expr():
            childresult = self.visit(node)
            childrenResults.append(childresult)

        if childrenResults[0] == "Int" and childrenResults[-1] == "Int":
            return "Int"
        else:
            error = semanticError(ctx.start.line, "Cannot add " + childrenResults[0] + " and " + childrenResults[-1])
            self.foundErrors.append(error)
            return "Error"

    # Visit a parse tree produced by YAPL2Parser#isVoidExpr.
    def visitIsVoidExpr(self, ctx:YAPL2Parser.IsVoidExprContext):
        result = self.visit(ctx.expr())
        return "Bool"


    # Visit a parse tree produced by YAPL2Parser#objectIdExpr.
    def visitObjectIdExpr(self, ctx:YAPL2Parser.ObjectIdExprContext):
        varName = str(ctx.OBJECTID())
        if varName == "self":
            return "SELF_TYPE"
        #search for varName in attribute table
        else:
            varEntry = self.attributeTable.findEntry(varName, self.currentClass, self.currentMethodId,self.currentScope)  
            if self.currentScope == 3:
                if varEntry is None:
                    varEntry = self.attributeTable.findEntry(varName, self.currentClass, self.currentMethodId,self.currentScope-1)
                if varEntry is None and self.currentScope > 1:
                    varEntry = self.attributeTable.findEntry(varName, self.currentClass, None,self.currentScope-2)    
                if varEntry is None:
                    error = semanticError(ctx.start.line, "Variable " + varName + " not defined")
                    self.foundErrors.append(error)
                    return "Error"
                else:
                    return varEntry.type
            else:
                if varEntry is None:
                    varEntry = self.attributeTable.findEntry(varName, self.currentClass, None, self.currentScope -1)
                if varEntry is None:
                    error = semanticError(ctx.start.line, "Variable " + varName + " not defined")
                    self.foundErrors.append(error)
                    return "Error"
                else:
                    return varEntry.type

    # Visit a parse tree produced by YAPL2Parser#substractExpr.
    def visitSubstractExpr(self, ctx:YAPL2Parser.SubstractExprContext):
        childrenResults = []
        for node in ctx.expr():
            childresult = self.visit(node)
            childrenResults.append(childresult)

        if childrenResults[0] == "Int" and childrenResults[-1] == "Int":
            return "Int"
        else:
            error = semanticError(ctx.start.line, "Cannot subtract " + childrenResults[0] + " and " + childrenResults[-1])
            self.foundErrors.append(error)
            return "Error"


    # Visit a parse tree produced by YAPL2Parser#falseExpr.
    def visitFalseExpr(self, ctx:YAPL2Parser.FalseExprContext):
        return "Bool"


    # Visit a parse tree produced by YAPL2Parser#parenthExpr.
    def visitParenthExpr(self, ctx:YAPL2Parser.ParenthExprContext):
        result = self.visit(ctx.expr())
        return result


    # Visit a parse tree produced by YAPL2Parser#equalExpr.
    def visitEqualExpr(self, ctx:YAPL2Parser.EqualExprContext):
        childrenResults = []
        for node in ctx.expr():
            childrenResults.append(self.visit(node))
        if childrenResults[0] == "Int" and childrenResults[1] == "Int":
            return "Bool"
        else:
            error = semanticError(ctx.start.line, "Cannot compare " + childrenResults[0] + " and " + childrenResults[1])
            self.foundErrors.append(error)
            return "Error"



del YAPL2Parser