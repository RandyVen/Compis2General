from YAPLVisitor import *
from errors import semanticError
from YAPLParser import *

from table.attribute_table import *
from table.class_table import *
from table.function_table import *
from table.types_table import *

attributeTable = AttributeTable()
typesTable = TypesTable()
classTable = ClassTable()
functionTable = FunctionTable()

class YaplVisitorEditedBase(YAPLVisitor):
    def visitClass(self, ctx:YAPLParser.ClassExprContext):
        className = ctx.TYPEID()[0]
        entry = ClassTableEntry(className)
        classTable.addEntry(entry)
        return self.visitChildren(ctx)

    def visitMethod(self, ctx:YAPLParser.MethodContext):
         functionName = ctx.OBJECTID()
         type = ctx.TYPEID()
         entry = FunctionTableEntry(functionName, type)
         functionTable.addEntry(entry)
         return self.visitChildren(ctx)
    
    def visitFeature(self, ctx:YAPLParser.FeatureContext):
        featureName = ctx.OBJECTID()
        featureType = ctx.TYPEID()
        entry = AttributeTableEntry(featureName, featureType)
        attributeTable.addEntry(entry)
        return self.visitChildren(ctx)

    def visitFormal(self, ctx:YAPLParser.FormalContext):
         featureName = ctx.OBJECTID()
         featureType = ctx.TYPEID()
         entry = AttributeTableEntry(featureName, featureType)
         attributeTable.addEntry(entry)
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
