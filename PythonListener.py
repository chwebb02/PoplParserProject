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



del PythonParser