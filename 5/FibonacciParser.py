# Generated from Fibonacci.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,13,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        2,0,2,0,0,10,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,
        1,0,0,0,7,8,5,1,0,0,8,9,5,2,0,0,9,10,5,4,0,0,10,11,5,3,0,0,11,3,
        1,0,0,0,0
    ]

class FibonacciParser ( Parser ):

    grammarFileName = "Fibonacci.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'FIBO'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "WS" ]

    RULE_prog = 0
    RULE_fibo = 1

    ruleNames =  [ "prog", "fibo" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NUM=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fibo(self):
            return self.getTypedRuleContext(FibonacciParser.FiboContext,0)


        def EOF(self):
            return self.getToken(FibonacciParser.EOF, 0)

        def getRuleIndex(self):
            return FibonacciParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = FibonacciParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.fibo()
            self.state = 5
            self.match(FibonacciParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FiboContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(FibonacciParser.NUM, 0)

        def getRuleIndex(self):
            return FibonacciParser.RULE_fibo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFibo" ):
                listener.enterFibo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFibo" ):
                listener.exitFibo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFibo" ):
                return visitor.visitFibo(self)
            else:
                return visitor.visitChildren(self)




    def fibo(self):

        localctx = FibonacciParser.FiboContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fibo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(FibonacciParser.T__0)
            self.state = 8
            self.match(FibonacciParser.T__1)
            self.state = 9
            self.match(FibonacciParser.NUM)
            self.state = 10
            self.match(FibonacciParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





