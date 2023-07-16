# Generated from YAPL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.

class YAPLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YAPLParser#start.
    def visitStart(self, ctx:YAPLParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx:YAPLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#classExpr.
    def visitClassExpr(self, ctx:YAPLParser.ClassExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#method.
    def visitMethod(self, ctx:YAPLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#attribute.
    def visitAttribute(self, ctx:YAPLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx:YAPLParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#add.
    def visitAdd(self, ctx:YAPLParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#new.
    def visitNew(self, ctx:YAPLParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#negation.
    def visitNegation(self, ctx:YAPLParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#dispatch.
    def visitDispatch(self, ctx:YAPLParser.DispatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#string.
    def visitString(self, ctx:YAPLParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#assignment.
    def visitAssignment(self, ctx:YAPLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#false.
    def visitFalse(self, ctx:YAPLParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#integer.
    def visitInteger(self, ctx:YAPLParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#while.
    def visitWhile(self, ctx:YAPLParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#parenthesis.
    def visitParenthesis(self, ctx:YAPLParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#equal.
    def visitEqual(self, ctx:YAPLParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#not.
    def visitNot(self, ctx:YAPLParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#isVoid.
    def visitIsVoid(self, ctx:YAPLParser.IsVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#function.
    def visitFunction(self, ctx:YAPLParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessThan.
    def visitLessThan(self, ctx:YAPLParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#bracket.
    def visitBracket(self, ctx:YAPLParser.BracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#true.
    def visitTrue(self, ctx:YAPLParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#let.
    def visitLet(self, ctx:YAPLParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#divide.
    def visitDivide(self, ctx:YAPLParser.DivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#id.
    def visitId(self, ctx:YAPLParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessEqual.
    def visitLessEqual(self, ctx:YAPLParser.LessEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#multiply.
    def visitMultiply(self, ctx:YAPLParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#ifElse.
    def visitIfElse(self, ctx:YAPLParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#substract.
    def visitSubstract(self, ctx:YAPLParser.SubstractContext):
        return self.visitChildren(ctx)



del YAPLParser