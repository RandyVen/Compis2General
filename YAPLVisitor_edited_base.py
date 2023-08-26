from YAPLVisitor import *
from errors import semanticError
from YAPLParser import *

from table.attribute_table import *
from table.class_table import *
from table.function_table import *
from table.types_table import *
from errors import semanticError

class YaplVisitorEditedBase(YAPLVisitor):

    def __init__(self):
        super().__init__()
        self.functionTable = FunctionTable()
        self.attributeTable = AttributeTable()
        self.typesTable = TypesTable()
        self.classTable = ClassTable()
        self.currentMethod = None
        self.currentScope = 1
        self.currentClass = "Debugg"
        self.currentMethodId = 0
        self.foundErrors = []
    
    def visitClass(self, ctx:YAPLParser.ClassExprContext):

        className = str(ctx.TYPEID()[0])
        if len(ctx.TYPEID()) > 1:
            parentClass = str(ctx.TYPEID()[1])
        else:
            parentClass = None
        entry = ClassTableEntry(className, parentClass)
        self.classTable.addEntry(entry)
        self.currentClass = className
        self.currentMethod = None
        self.currentScope = 1
        return self.visitChildren(ctx)

    def visitMethod(self, ctx:YAPLParser.MethodContext): 

        self.currentMethodId += 1

        functionName = str(ctx.ID())
        type = str(ctx.TYPEID())
        entry = FunctionTableEntry(self.currentMethodId,functionName, type, currentScope, self.currentClass)
        self.functionTable.addEntry(entry)
        self.currentMethod = functionName
        currentScope = 2
        return self.visitChildren(ctx)
    
    def visitFeature(self, ctx:YAPLParser.FeatureContext):

  
        featureName = str(ctx.ID())
        featureType = str(ctx.TYPEID())
        if self.currentMethod:
            entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, self.currentMethodId)
        else:
            entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, None)
        self.attributeTable.addEntry(entry)

        return self.visitChildren(ctx)

    def visitFormal(self, ctx:YAPLParser.FormalContext):

        featureName = str(ctx.ID())
        featureType = str(ctx.TYPEID())
        entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, self.currentMethodId)
        self.attributeTable.addEntry(entry)
        return self.visitChildren(ctx)

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

    # Visit a parse tree produced by YAPL2Parser#lessExpr.
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


    # Visit a parse tree produced by YAPLParser#substract.
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

    def visitInteger(self, ctx:YAPLParser.IntegerContext):
         return "Int"
    
    # Visit a parse tree produced by YAPL2Parser#trueExpr.
    def visitTrue(self, ctx:YAPLParser.TrueContext):
        return "Bool"
    
    def visitFalseExpr(self, ctx:YAPLParser.FalseContext):
        return "Bool"
        
    def visitAssignment(self, ctx:YAPLParser.AssignmentContext):

         leftside = str(ctx.ID())
         #search for leftside in attribute table
         leftsideEntry = self.attributeTable.findEntry(leftside, self.currentClass, self.currentMethodId)
         #if not found, search without methdod
         if leftsideEntry is None:
             leftsideEntry = self.attributeTable.findEntry(leftside, self.currentClass, None)
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

    def visitId(self, ctx:YAPLParser.IdContext):

         varName = str(ctx.ID())
         if varName == "self":
             return "SELF_TYPE"
         #search for varName in attribute table
         else:
             varEntry = self.attributeTable.findEntry(varName, self.currentClass, self.currentMethodId)  
             if varEntry is None:
                 varEntry = self.attributeTable.findEntry(varName, self.currentClass, None)
             if varEntry is None:
                 error = semanticError(ctx.start.line, "Variable " + varName + " not defined")
                 self.foundErrors.append(error)
                 return "Error"
             else:
                 return varEntry.type

    def visitString(self, ctx:YAPLParser.StringExprContext):
         return "String"
    
    def visitNot(self, ctx:YAPLParser.NotContext):
        childrenResult = self.visit(ctx.expr())
        if childrenResult == "Bool":
            return "Bool"
        else:
            error = semanticError(ctx.start.line, "Cannot use NOT operator on  " + childrenResult)
            self.foundErrors.append(error)
            return "Error"