from FibonacciVisitor import FibonacciVisitor
from FibonacciParser import FibonacciParser

class FibonacciVisitorImpl(FibonacciVisitor):

    def visitProg(self, ctx:FibonacciParser.ProgContext):
        return self.visit(ctx.fibo())

    def visitFibo(self, ctx:FibonacciParser.FiboContext):
        n = int(ctx.NUM().getText())

        fib = []
        a, b = 0, 1

        for i in range(n):
            fib.append(a)
            a, b = b, a + b

        print(", ".join(map(str, fib)))
