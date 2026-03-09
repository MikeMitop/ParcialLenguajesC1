import sys
from antlr4 import *

from FibonacciLexer import FibonacciLexer
from FibonacciParser import FibonacciParser
from FibonacciVisitorImpl import FibonacciVisitorImpl


def main():

    print("Ingrese la expresión (ej: FIBO(8)):")

    entrada = input()

    input_stream = InputStream(entrada)

    lexer = FibonacciLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = FibonacciParser(stream)
    tree = parser.prog()

    visitor = FibonacciVisitorImpl()
    visitor.visit(tree)


if __name__ == '__main__':
    main()
