# Generated from YAPL2.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.
from table.attribute_table import *
from table.types_table import *
from table.class_table import *
from table.function_table import *
from errors import semanticError

class YaplVisitorNew(ParseTreeVisitor):
    
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

    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx:YAPLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#classDEF.
    def visitClassExpr(self, ctx:YAPLParser.ClassExprContext):
        className = str(ctx.TYPE()[0])
        if len(ctx.TYPE()) > 1:
            parentClass = str(ctx.TYPE()[1])
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


    # Visit a parse tree produced by YAPLParser#MethodDef.
    def visitMethod(self, ctx:YAPLParser.MethodContext):
        self.currentMethodId += 1
        functionName = str(ctx.ID())
        type = str(ctx.TYPE())
        if type == "SELF_TYPE":
            print("SELF_TYPE")
            type = self.currentClass
        # entry = FunctionTableEntry(self.currentMethodId,functionName, type, self.currentScope, self.currentClass)
        # self.functionTable.addEntry(entry)
        self.currentMethod = functionName
        self.currentScope = 2
        for node in ctx.formal():
            self.visit(node)
        childrenResult = self.visit(ctx.expr())
        if childrenResult == type:
            return type
        else:
            error = semanticError(ctx.start.line, "Function " + functionName + " returns " + childrenResult + " instead of " + type)
            self.foundErrors.append(error)
            return "Error"

    # Visit a parse tree produced by YAPLParser#FeactureDecalration.
    def visitFeature(self, ctx:YAPLParser.FeatureContext):
        # featureName = str(ctx.ID())
        # featureType = str(ctx.TYPE())
        # if self.currentMethod:
        #     entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, self.currentMethodId)
        # else:
        #     entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, None)
        # self.attributeTable.addEntry(entry)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx:YAPLParser.FormalContext):
        # featureName = str(ctx.ID())
        # featureType = str(ctx.TYPE())
        # entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, self.currentMethodId, True)
        # self.attributeTable.addEntry(entry)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#newExpr.
    def visitNew(self, ctx:YAPLParser.NewContext):
        classType = str(ctx.TYPE())
        if self.classTable.findEntry(classType):
            return classType
        else:
            if self.typesTable.findEntry(classType):
                return classType
            else:
                error = semanticError(ctx.start.line, "Class " + classType + " not defined")
                self.foundErrors.append(error)
                return "Error"


    # Visit a parse tree produced by YAPLParser#divideExpr.
    def visitDivide(self, ctx:YAPLParser.DivideContext):
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


    # Visit a parse tree produced by YAPLParser#FunctionExpr.
    def visitFunction(self, ctx:YAPLParser.FunctionContext):
        childrenResults = []
        for node in ctx.expr():
            childresult = self.visit(node)
            childrenResults.append(childresult)
        #Check if the function is defined
        methodEntry = self.functionTable.findEntryByName(str(ctx.ID()), self.currentClass)
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
            return methodEntry.type
        #Else check if the function belongs to a parent class
        else:
            usingClass = self.classTable.findEntry(self.currentClass)
            if usingClass:
                parrentClass = usingClass.inherits
                if parrentClass:
                    methodEntry = self.functionTable.findEntryByName(str(ctx.ID()), parrentClass)
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
                        return methodEntry.type
                    else:
                        error = semanticError(ctx.start.line, "Function " + str(ctx.ID()) + " not defined")
                        self.foundErrors.append(error)
                        return "Error"
                else:
                    error = semanticError(ctx.start.line, "Function " + str(ctx.ID()) + " not defined")
                    self.foundErrors.append(error)
                    return "Error"
            else:
                return "Error"


    # Visit a parse tree produced by YAPLParser#integerExpr.
    def visitInteger(self, ctx:YAPLParser.IntegerContext):
        return "Int"


    # Visit a parse tree produced by YAPLParser#trueExpr.
    def visitTrue(self, ctx:YAPLParser.TrueContext):
        return "Bool"


    # Visit a parse tree produced by YAPLParser#MethodExpr.
    def visitMethod(self, ctx:YAPLParser.MethodContext):
        childrenResults = []
        for node in ctx.expr():
            childresult = self.visit(node)
            childrenResults.append(childresult)
        mainClass = childrenResults[0]
        #Check if we are using a method from a parent class
        if ctx.TYPE():
            parentClass = str(ctx.TYPE())
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
            methodEntry =  self.functionTable.findEntryByName(str(ctx.ID()), parentClass)
            if methodEntry:
                params = childrenResults[1:]
                print(methodEntry.id)
                savedParams = self.attributeTable.findParamsOfFunction(methodEntry.id)
                print(savedParams)
                if len(params) != len(savedParams):
                    error = semanticError(ctx.start.line, "Function " + methodEntry.name + " expects " + str(len(savedParams)) + " parameters but " + str(len(params)) + " were given")
                    self.foundErrors.append(error)
                    return "Error"
                for i in range(len(params)):
                    if params[i] != savedParams[i].type:
                        error = semanticError(ctx.start.line, "Function " + methodEntry.name + " expects " + savedParams[i].type + " as parameter " + str(i+1) + " but " + params[i] + " was given")
                        self.foundErrors.append(error)
                        return "Error"
                return methodEntry.type
            else:
                error = semanticError(ctx.start.line, "Method " + str(ctx.ID()) + " not defined in " + parentClass)
                self.foundErrors.append(error)
                return "Error"
        else:
            # Check if the method is defined in the current class
            methodEntry = self.functionTable.findEntryByName(str(ctx.ID()), mainClass)
            if methodEntry:
                params = childrenResults[1:]
                print(methodEntry.id)
                savedParams = self.attributeTable.findParamsOfFunction(methodEntry.id)
                print(savedParams)
                if len(params) != len(savedParams):
                    error = semanticError(ctx.start.line, "Function " + methodEntry.name + " expects " + str(len(savedParams)) + " parameters but " + str(len(params)) + " were given")
                    self.foundErrors.append(error)
                    return "Error"
                for i in range(len(params)):
                    if params[i] != savedParams[i].type:
                        error = semanticError(ctx.start.line, "Function " + methodEntry.name + " expects " + savedParams[i].type + " as parameter " + str(i+1) + " but " + params[i] + " was given")
                        self.foundErrors.append(error)
                        return "Error"
                return methodEntry.type
            else:
                error = semanticError(ctx.start.line, "Method " + str(ctx.ID()) + " not defined in " + mainClass)
                self.foundErrors.append(error)
                return "Error"

    # Visit a parse tree produced by YAPLParser#DeclarationExpression.
    def visitExpr(self, ctx:YAPLParser.ExprContext):
        leftside = str(ctx.ID())
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
        if childrenResult == leftsideEntry.type:
            return leftsideEntry.type
        else:
            error = semanticError(ctx.start.line, "Can't assign " + childrenResult + " to " + leftsideEntry.type)
            self.foundErrors.append(error)
            return "Error"
        
    # Visit a parse tree produced by YAPLParser#ifElseExpr.
    def visitIfElse(self, ctx:YAPLParser.IfElseContext):
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

    # Visit a parse tree produced by YAPLParser#lessExpr.
    def visitLess(self, ctx:YAPLParser.LessEqualContext):
        childrenResults = []
        for node in ctx.expr():
            childrenResults.append(self.visit(node))
        if childrenResults[0] == "Int" and childrenResults[1] == "Int":
            return "Bool"
        else:
            error = semanticError(ctx.start.line, "Cannot compare " + childrenResults[0] + " and " + childrenResults[1])
            self.foundErrors.append(error)
            return "Error"


    # Visit a parse tree produced by YAPLParser#BraketedExpr.
    def visitBraket(self, ctx:YAPLParser.BracketContext):
        childrenResults = []
        for node in ctx.expr():
            childrenResults.append(self.visit(node))
        
        return childrenResults[-1]


    # Visit a parse tree produced by YAPLParser#multiplyExpr.
    def visitMultiply(self, ctx:YAPLParser.MultiplyContext):
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


    # Visit a parse tree produced by YAPLParser#letExpr.
    def visitLet(self, ctx:YAPLParser.LetContext):
        self.currentScope = 3
        firstVisits = ctx.expr()[0:-1]
        firstVisitsResults = []
        for node in firstVisits:
            firstVisitsResults.append(self.visit(node))
        for i in range(len(ctx.ID())):
            newVarName = str(ctx.OBJECTID()[i])
            newVarType = str(ctx.TYPE()[i])
            # newVarEntry = AttributeTableEntry(newVarName, newVarType, self.currentScope, self.currentClass, self.currentMethodId)
            # self.attributeTable.addEntry(newVarEntry)
            if i < len(firstVisitsResults):
                if firstVisitsResults[i] != newVarType:
                    error = semanticError(ctx.start.line, "Can't assign " + firstVisitsResults[i] + " to " + newVarType)
                    self.foundErrors.append(error)
                    return "Error"
        lastExpresionResult = self.visit(ctx.expr()[-1])
        return lastExpresionResult



    # Visit a parse tree produced by YAPLParser#stringExpr.
    def visitString(self, ctx:YAPLParser.StringContext):
        return "String"


    # Visit a parse tree produced by YAPLParser#lessEqualExpr.
    def visitLessEqual(self, ctx:YAPLParser.LessEqualContext):
        childrenResults = []
        for node in ctx.expr():
            childrenResults.append(self.visit(node))
        if childrenResults[0] == "Int" and childrenResults[1] == "Int":
            return "Bool"
        else:
            error = semanticError(ctx.start.line, "Cannot compare " + childrenResults[0] + " and " + childrenResults[1])
            self.foundErrors.append(error)
            return "Error"
    


    # Visit a parse tree produced by YAPLParser#notExpr.
    def visitNot(self, ctx:YAPLParser.NotContext):
        childrenResult = self.visit(ctx.expr())
        if childrenResult == "Bool" or childrenResult == "Int":
            return childrenResult
        else:
            error = semanticError(ctx.start.line, "Cannot use NOT operator on  " + childrenResult)
            self.foundErrors.append(error)
            return "Error"

    # Visit a parse tree produced by YAPLParser#whileExpr.
    def visitWhile(self, ctx:YAPLParser.WhileContext):
        childrenResult = []
        for node in ctx.expr():
            childrenResult.append(self.visit(node))
        if childrenResult[0] == "Bool":
            return "Object"
        else:
            error = semanticError(ctx.start.line, "Cannot use " + childrenResult[0] + " as condition")
            self.foundErrors.append(error)
            return "Error"

    # Visit a parse tree produced by YAPLParser#addExpr.
    def visitAdd(self, ctx:YAPLParser.AddContext):
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

    # Visit a parse tree produced by YAPLParser#isVoidExpr.
    def visitIsVoid(self, ctx:YAPLParser.IsVoidContext):
        result = self.visit(ctx.expr())
        return "Bool"


    # Visit a parse tree produced by YAPLParser#objectIdExpr.
    def visitId(self, ctx:YAPLParser.IdContext):
        varName = str(ctx.OBJECTID())
        if varName == "self":
            return self.currentClass
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

    # Visit a parse tree produced by YAPLParser#substractExpr.
    def visitSubstract(self, ctx:YAPLParser.SubstractContext):
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


    # Visit a parse tree produced by YAPLParser#falseExpr.
    def visitFalse(self, ctx:YAPLParser.FalseContext):
        return "Bool"


    # Visit a parse tree produced by YAPLParser#parenthExpr.
    def visitParenthesis(self, ctx:YAPLParser.ParenthesisContext):
        result = self.visit(ctx.expr())
        return result


    # Visit a parse tree produced by YAPLParser#equalExpr.
    def visitEqual(self, ctx:YAPLParser.EqualContext):
        childrenResults = []
        for node in ctx.expr():
            childrenResults.append(self.visit(node))
        if childrenResults[0] == "Int" and childrenResults[1] == "Int":
            return "Bool"
        else:
            error = semanticError(ctx.start.line, "Cannot compare " + childrenResults[0] + " and " + childrenResults[1])
            self.foundErrors.append(error)
            return "Error"



del YAPLParser
