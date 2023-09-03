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

class FirstVisitor(ParseTreeVisitor):
    
    def __init__(self):
        super().__init__()
        self.functionTable = FunctionTable()
        self.attributeTable = AttributeTable()
        self.typesTable = TypesTable()
        self.classTable = ClassTable()
        self.currentMethod = None
        self.currentScope = 1
        self.currentClass = "Debugg"
        self.currentMethodId = 10
        self.foundErrors = []

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
        if parentClass:
            entry = ClassTableEntry(className, parentClass)
        else:
            entry = ClassTableEntry(className)
        self.classTable.addEntry(entry)
        self.currentClass = className
        self.currentMethod = None
        self.currentScope = 1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#MethodDef.
    def visitMethodDef(self, ctx:YAPL2Parser.MethodDefContext):
        self.currentMethodId += 1
        functionName = str(ctx.OBJECTID())
        type = str(ctx.TYPEID())
        entry = FunctionTableEntry(self.currentMethodId,functionName, type, self.currentScope, self.currentClass)
        self.functionTable.addEntry(entry)
        self.currentMethod = functionName
        self.currentScope = 2
        for node in ctx.formal():
            self.visit(node)
        return self.visit(ctx.expr())

    # Visit a parse tree produced by YAPL2Parser#FeactureDecalration.
    def visitFeactureDecalration(self, ctx:YAPL2Parser.FeactureDecalrationContext):
        featureName = str(ctx.OBJECTID())
        featureType = str(ctx.TYPEID())
        if self.currentMethod:
            entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, self.currentMethodId)
        else:
            entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, None)
        self.attributeTable.addEntry(entry)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#formal.
    def visitFormal(self, ctx:YAPL2Parser.FormalContext):
        featureName = str(ctx.OBJECTID())
        featureType = str(ctx.TYPEID())
        entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, self.currentMethodId, True)
        self.attributeTable.addEntry(entry)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#newExpr.
    def visitNewExpr(self, ctx:YAPL2Parser.NewExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#divideExpr.
    def visitDivideExpr(self, ctx:YAPL2Parser.DivideExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#FunctionExpr.
    def visitFunctionExpr(self, ctx:YAPL2Parser.FunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#integerExpr.
    def visitIntegerExpr(self, ctx:YAPL2Parser.IntegerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#trueExpr.
    def visitTrueExpr(self, ctx:YAPL2Parser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#MethodExpr.
    def visitMethodExpr(self, ctx:YAPL2Parser.MethodExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPL2Parser#DeclarationExpression.
    def visitDeclarationExpression(self, ctx:YAPL2Parser.DeclarationExpressionContext):
        return self.visitChildren(ctx)
        
    # Visit a parse tree produced by YAPL2Parser#ifElseExpr.
    def visitIfElseExpr(self, ctx:YAPL2Parser.IfElseExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPL2Parser#lessExpr.
    def visitLessExpr(self, ctx:YAPL2Parser.LessExprContext):
       return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#BraketedExpr.
    def visitBraketedExpr(self, ctx:YAPL2Parser.BraketedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#multiplyExpr.
    def visitMultiplyExpr(self, ctx:YAPL2Parser.MultiplyExprContext):
        return self.visitChildren(ctx)


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
            newVarEntry = AttributeTableEntry(newVarName, newVarType, self.currentScope, self.currentClass, self.currentMethodId)
            self.attributeTable.addEntry(newVarEntry)
        return self.visitChildren(ctx)



    # Visit a parse tree produced by YAPL2Parser#stringExpr.
    def visitStringExpr(self, ctx:YAPL2Parser.StringExprContext):
        return "String"


    # Visit a parse tree produced by YAPL2Parser#lessEqualExpr.
    def visitLessEqualExpr(self, ctx:YAPL2Parser.LessEqualExprContext):
        return self.visitChildren(ctx)
    


    # Visit a parse tree produced by YAPL2Parser#notExpr.
    def visitNotExpr(self, ctx:YAPL2Parser.NotExprContext):
       return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPL2Parser#whileExpr.
    def visitWhileExpr(self, ctx:YAPL2Parser.WhileExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPL2Parser#addExpr.
    def visitAddExpr(self, ctx:YAPL2Parser.AddExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPL2Parser#isVoidExpr.
    def visitIsVoidExpr(self, ctx:YAPL2Parser.IsVoidExprContext):
        result = self.visit(ctx.expr())
        return "Bool"


    # Visit a parse tree produced by YAPL2Parser#objectIdExpr.
    def visitObjectIdExpr(self, ctx:YAPL2Parser.ObjectIdExprContext):
       return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPL2Parser#substractExpr.
    def visitSubstractExpr(self, ctx:YAPL2Parser.SubstractExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#falseExpr.
    def visitFalseExpr(self, ctx:YAPL2Parser.FalseExprContext):
        return "Bool"


    # Visit a parse tree produced by YAPL2Parser#parenthExpr.
    def visitParenthExpr(self, ctx:YAPL2Parser.ParenthExprContext):
       return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#equalExpr.
    def visitEqualExpr(self, ctx:YAPL2Parser.EqualExprContext):
        return self.visitChildren(ctx)



del YAPL2Parser