# Generated from Python.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("*\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\7\2\f\n\2\f\2\16")
        buf.write("\2\17\13\2\3\2\5\2\22\n\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\5\4\33\n\4\3\5\3\5\3\5\5\5 \n\5\3\5\3\5\3\5\7\5%\n\5")
        buf.write("\f\5\16\5(\13\5\3\5\2\3\b\6\2\4\6\b\2\2\2+\2\21\3\2\2")
        buf.write("\2\4\23\3\2\2\2\6\32\3\2\2\2\b\37\3\2\2\2\n\f\5\4\3\2")
        buf.write("\13\n\3\2\2\2\f\17\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16")
        buf.write("\22\3\2\2\2\17\r\3\2\2\2\20\22\7\2\2\3\21\r\3\2\2\2\21")
        buf.write("\20\3\2\2\2\22\3\3\2\2\2\23\24\7\4\2\2\24\25\7\5\2\2\25")
        buf.write("\26\5\6\4\2\26\5\3\2\2\2\27\33\7\6\2\2\30\33\5\b\5\2\31")
        buf.write("\33\7\4\2\2\32\27\3\2\2\2\32\30\3\2\2\2\32\31\3\2\2\2")
        buf.write("\33\7\3\2\2\2\34\35\b\5\1\2\35 \7\6\2\2\36 \7\4\2\2\37")
        buf.write("\34\3\2\2\2\37\36\3\2\2\2 &\3\2\2\2!\"\f\3\2\2\"#\7\r")
        buf.write("\2\2#%\5\b\5\4$!\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2")
        buf.write("\2\'\t\3\2\2\2(&\3\2\2\2\7\r\21\32\37&")
        return buf.getvalue()


class PythonParser ( Parser ):

    grammarFileName = "Python.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "WS", "IDENTIFIER", "ASSIGN_OP", "LITERAL", 
                      "STR_LIT", "INT_LIT", "FLOAT_LIT", "LIST_LIT", "LIST_ELEMENT", 
                      "BOOLEAN_LIT", "ARITH_OP" ]

    RULE_prog = 0
    RULE_assignment = 1
    RULE_value = 2
    RULE_expr = 3

    ruleNames =  [ "prog", "assignment", "value", "expr" ]

    EOF = Token.EOF
    WS=1
    IDENTIFIER=2
    ASSIGN_OP=3
    LITERAL=4
    STR_LIT=5
    INT_LIT=6
    FLOAT_LIT=7
    LIST_LIT=8
    LIST_ELEMENT=9
    BOOLEAN_LIT=10
    ARITH_OP=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(PythonParser.AssignmentContext,i)


        def EOF(self):
            return self.getToken(PythonParser.EOF, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = PythonParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.state = 15
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PythonParser.IDENTIFIER:
                    self.state = 8
                    self.assignment()
                    self.state = 13
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(PythonParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PythonParser.IDENTIFIER, 0)

        def ASSIGN_OP(self):
            return self.getToken(PythonParser.ASSIGN_OP, 0)

        def value(self):
            return self.getTypedRuleContext(PythonParser.ValueContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = PythonParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(PythonParser.IDENTIFIER)
            self.state = 18
            self.match(PythonParser.ASSIGN_OP)
            self.state = 19
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL(self):
            return self.getToken(PythonParser.LITERAL, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def IDENTIFIER(self):
            return self.getToken(PythonParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = PythonParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_value)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(PythonParser.LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(PythonParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL(self):
            return self.getToken(PythonParser.LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(PythonParser.IDENTIFIER, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParser.ExprContext,i)


        def ARITH_OP(self):
            return self.getToken(PythonParser.ARITH_OP, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PythonParser.LITERAL]:
                self.state = 27
                self.match(PythonParser.LITERAL)
                pass
            elif token in [PythonParser.IDENTIFIER]:
                self.state = 28
                self.match(PythonParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 31
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 32
                    self.match(PythonParser.ARITH_OP)
                    self.state = 33
                    self.expr(2) 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




