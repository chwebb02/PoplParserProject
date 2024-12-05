# Generated from Python.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#prog.
    def enterProg(self, ctx:PythonParser.ProgContext):
        pass

    # Exit a parse tree produced by PythonParser#prog.
    def exitProg(self, ctx:PythonParser.ProgContext):
        pass


    # Enter a parse tree produced by PythonParser#statement.
    def enterStatement(self, ctx:PythonParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonParser#statement.
    def exitStatement(self, ctx:PythonParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonParser#assignment.
    def enterAssignment(self, ctx:PythonParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PythonParser#assignment.
    def exitAssignment(self, ctx:PythonParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PythonParser#value.
    def enterValue(self, ctx:PythonParser.ValueContext):
        pass

    # Exit a parse tree produced by PythonParser#value.
    def exitValue(self, ctx:PythonParser.ValueContext):
        pass


    # Enter a parse tree produced by PythonParser#expr.
    def enterExpr(self, ctx:PythonParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonParser#expr.
    def exitExpr(self, ctx:PythonParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonParser#conditional.
    def enterConditional(self, ctx:PythonParser.ConditionalContext):
        pass

    # Exit a parse tree produced by PythonParser#conditional.
    def exitConditional(self, ctx:PythonParser.ConditionalContext):
        pass


    # Enter a parse tree produced by PythonParser#cond_if.
    def enterCond_if(self, ctx:PythonParser.Cond_ifContext):
        pass

    # Exit a parse tree produced by PythonParser#cond_if.
    def exitCond_if(self, ctx:PythonParser.Cond_ifContext):
        pass


    # Enter a parse tree produced by PythonParser#cond_elif.
    def enterCond_elif(self, ctx:PythonParser.Cond_elifContext):
        pass

    # Exit a parse tree produced by PythonParser#cond_elif.
    def exitCond_elif(self, ctx:PythonParser.Cond_elifContext):
        pass


    # Enter a parse tree produced by PythonParser#cond_else.
    def enterCond_else(self, ctx:PythonParser.Cond_elseContext):
        pass

    # Exit a parse tree produced by PythonParser#cond_else.
    def exitCond_else(self, ctx:PythonParser.Cond_elseContext):
        pass


    # Enter a parse tree produced by PythonParser#then.
    def enterThen(self, ctx:PythonParser.ThenContext):
        pass

    # Exit a parse tree produced by PythonParser#then.
    def exitThen(self, ctx:PythonParser.ThenContext):
        pass


    # Enter a parse tree produced by PythonParser#indented_statement.
    def enterIndented_statement(self, ctx:PythonParser.Indented_statementContext):
        pass

    # Exit a parse tree produced by PythonParser#indented_statement.
    def exitIndented_statement(self, ctx:PythonParser.Indented_statementContext):
        pass


    # Enter a parse tree produced by PythonParser#boolean_expr.
    def enterBoolean_expr(self, ctx:PythonParser.Boolean_exprContext):
        pass

    # Exit a parse tree produced by PythonParser#boolean_expr.
    def exitBoolean_expr(self, ctx:PythonParser.Boolean_exprContext):
        pass


    # Enter a parse tree produced by PythonParser#loop.
    def enterLoop(self, ctx:PythonParser.LoopContext):
        pass

    # Exit a parse tree produced by PythonParser#loop.
    def exitLoop(self, ctx:PythonParser.LoopContext):
        pass


    # Enter a parse tree produced by PythonParser#while_loop.
    def enterWhile_loop(self, ctx:PythonParser.While_loopContext):
        pass

    # Exit a parse tree produced by PythonParser#while_loop.
    def exitWhile_loop(self, ctx:PythonParser.While_loopContext):
        pass


    # Enter a parse tree produced by PythonParser#for_loop.
    def enterFor_loop(self, ctx:PythonParser.For_loopContext):
        pass

    # Exit a parse tree produced by PythonParser#for_loop.
    def exitFor_loop(self, ctx:PythonParser.For_loopContext):
        pass


    # Enter a parse tree produced by PythonParser#iterator.
    def enterIterator(self, ctx:PythonParser.IteratorContext):
        pass

    # Exit a parse tree produced by PythonParser#iterator.
    def exitIterator(self, ctx:PythonParser.IteratorContext):
        pass


    # Enter a parse tree produced by PythonParser#range_func.
    def enterRange_func(self, ctx:PythonParser.Range_funcContext):
        pass

    # Exit a parse tree produced by PythonParser#range_func.
    def exitRange_func(self, ctx:PythonParser.Range_funcContext):
        pass



del PythonParser