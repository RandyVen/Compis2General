from YAPLVisitor import *
from errors import semanticError
from YAPLParser import *

from table.attribute_table import *
from table.class_table import *
from table.function_table import *
from table.types_table import *
from errors import semanticError

attributeTable = AttributeTable()
typesTable = TypesTable()
classTable = ClassTable()
functionTable = FunctionTable()
currentScope = 1 
currentClass = "Debugg" 
currentMethod = "Debugg" 
currentMethodId = 0 
currentMethod = None
foundErrors = []

class YaplVisitorEditedBase(YAPLVisitor):
    def visitClass(self, ctx:YAPLParser.ClassExprContext):
        global currentClass
        global currentMethod
        global currentScope
        className = str(ctx.TYPEID()[0])
        if len(ctx.TYPEID()) > 1:
            parentClass = str(ctx.TYPEID()[1])
        else:
            parentClass = None
        entry = ClassTableEntry(className, parentClass)
        classTable.addEntry(entry)
        currentClass = className
        currentMethod = None
        currentScope = 1
        return self.visitChildren(ctx)

    def visitMethod(self, ctx:YAPLParser.MethodContext): 
        global currentMethod
        global currentScope
        global currentClass
        global currentMethodId
        currentMethodId += 1
        functionName = str(ctx.OBJECTID())
        type = str(ctx.TYPEID())
        entry = FunctionTableEntry(currentMethodId,functionName, type, currentScope, currentClass)
        functionTable.addEntry(entry)
        currentMethod = functionName
        currentScope = 2
        return self.visitChildren(ctx)
    
    def visitFeature(self, ctx:YAPLParser.FeatureContext):

        global currentMethod
        global currentScope
        global currentClass
        global currentMethodId
        featureName = str(ctx.OBJECTID())
        featureType = str(ctx.TYPEID())
        if currentMethod:
            entry = AttributeTableEntry(featureName, featureType, currentScope, currentClass, currentMethodId)
        else:
            entry = AttributeTableEntry(featureName, featureType, currentScope, currentClass, None)
        attributeTable.addEntry(entry)

        return self.visitChildren(ctx)

    def visitFormal(self, ctx:YAPLParser.FormalContext):
        global currentMethod
        global currentClass
        global currentScope
        featureName = str(ctx.OBJECTID())
        featureType = str(ctx.TYPEID())
        entry = AttributeTableEntry(featureName, featureType, currentScope, currentClass, currentMethodId)
        attributeTable.addEntry(entry)
        return self.visitChildren(ctx)

    def visitAdd(self, ctx:YAPLParser.AddContext):
        global foundErrors
        childrenResults = []
        for node in ctx.expr():
            childresult = self.visit(node)
            childrenResults.append(childresult)

        if childrenResults[0] == "Int" and childrenResults[-1] == "Int":
            return "Int"
        else:
            error = semanticError(ctx.start.line, "Cannot add " + childrenResults[0] + " and " + childrenResults[-1])
            foundErrors.append(error)
            return "Error"
        
    
     # Visit a parse tree produced by YAPLParser#equal.
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



    # Visit a parse tree produced by YAPLParser#not.
    def visitNot(self, ctx:YAPLParser.NotContext):
        childrenResult = self.visit(ctx.expr())
        if childrenResult == "Bool":
            return "Bool"
        else:
            error = semanticError(ctx.start.line, "Cannot use NOT operator on  " + childrenResult)
            self.foundErrors.append(error)
            return "Error"

   # Visit a parse tree produced by YAPLParser#lessThan.
    def visitLessThan(self, ctx:YAPLParser.LessThanContext):
        childrenResults = []
        for node in ctx.expr():
            childrenResults.append(self.visit(node))
        if childrenResults[0] == "Int" and childrenResults[1] == "Int":
            return "Bool"
        else:
            error = semanticError(ctx.start.line, "Cannot compare " + childrenResults[0] + " and " + childrenResults[1])
            self.foundErrors.append(error)
            return "Error"


    # Visit a parse tree produced by YAPLParser#divide.
    def visitDivide(self, ctx:YAPLParser.DivideContext):
        global foundErrors
        childrenResults = []
        for node in ctx.expr():
            childresult = self.visit(node)
            childrenResults.append(childresult)

        if childrenResults[0] == "Int" and childrenResults[-1] == "Int":
            return "Int"
        else:
            error = semanticError(ctx.start.line, "Cannot divide " + childrenResults[0] + " and " + childrenResults[-1])
            foundErrors.append(error)
            return "Error"


    # Visit a parse tree produced by YAPLParser#lessEqual.
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

    # Visit a parse tree produced by YAPLParser#multiply.
    def visitMultiply(self, ctx:YAPLParser.MultiplyContext):
         global foundErrors
         childrenResults = []
         for node in ctx.expr():
             childresult = self.visit(node)
             childrenResults.append(childresult)

         if childrenResults[0] == "Int" and childrenResults[-1] == "Int":
             return "Int"
         else:
             error = semanticError(ctx.start.line, "Cannot multiply " + childrenResults[0] + " and " + childrenResults[-1])
             foundErrors.append(error)
             return "Error"


    # Visit a parse tree produced by YAPLParser#substract.
    def visitSubstract(self, ctx:YAPLParser.SubstractContext):
        global foundErrors
        childrenResults = []
        for node in ctx.expr():
            childresult = self.visit(node)
            childrenResults.append(childresult)

        if childrenResults[0] == "Int" and childrenResults[-1] == "Int":
            return "Int"
        else:
            error = semanticError(ctx.start.line, "Cannot subtract " + childrenResults[0] + " and " + childrenResults[-1])
            foundErrors.append(error)
            return "Error"

    def visitInteger(self, ctx:YAPLParser.IntegerContext):
         return "Int"
    
    # Visit a parse tree produced by YAPL2Parser#trueExpr.
    def visitTrue(self, ctx:YAPLParser.TrueContext):
        return "Bool"
    
    def visitFalseExpr(self, ctx:YAPLParser.FalseContext):
        return "Bool"
        
    def visitAssignment(self, ctx:YAPLParser.AssignmentContext):
         global currentMethod
         global currentClass
         global currentScope
         global currentMethodId
         global foundErrors
         leftside = str(ctx.OBJECTID())
         #search for leftside in attribute table
         leftsideEntry = attributeTable.findEntry(leftside, currentClass, currentMethodId)
         #if not found, search without methdod
         if leftsideEntry is None:
             leftsideEntry = attributeTable.findEntry(leftside, currentClass, None)
         if leftsideEntry is None:
             error = semanticError(ctx.start.line, "Variable " + leftside + " not defined")
             foundErrors.append(error)
             return "Error"
         childrenResult = self.visitChildren(ctx)
         if childrenResult == leftsideEntry.type:
             return leftsideEntry.type
         else:
             error = semanticError(ctx.start.line, "Can't assign " + childrenResult + " to " + leftsideEntry.type)
             foundErrors.append(error)
             return "Error"

    def visitId(self, ctx:YAPLParser.IdContext):
         global currentMethod
         global currentClass
         global currentScope
         global currentMethodId
         global foundErrors
         varName = str(ctx.OBJECTID())
         if varName == "self":
             return "SELF_TYPE"
         #search for varName in attribute table
         else:
             varEntry = attributeTable.findEntry(varName, currentClass, currentMethodId)  
             if varEntry is None:
                 varEntry = attributeTable.findEntry(varName, currentClass, None)
             if varEntry is None:
                 error = semanticError(ctx.start.line, "Variable " + varName + " not defined")
                 foundErrors.append(error)
                 return "Error"
             else:
                 return varEntry.type