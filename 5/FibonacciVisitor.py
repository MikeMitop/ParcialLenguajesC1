# Generated from Fibonacci.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FibonacciParser import FibonacciParser
else:
    from FibonacciParser import FibonacciParser

# This class defines a complete generic visitor for a parse tree produced by FibonacciParser.

class FibonacciVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FibonacciParser#prog.
    def visitProg(self, ctx:FibonacciParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FibonacciParser#fibo.
    def visitFibo(self, ctx:FibonacciParser.FiboContext):
        return self.visitChildren(ctx)



del FibonacciParser