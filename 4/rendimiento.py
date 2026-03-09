import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

valores = [10, 20, 30, 40]

print("Comparacion de rendimiento en Python (Interpretado)")
for valor in valores:
    inicio = time.perf_counter()
    resultado = fibonacci(valor)
    fin = time.perf_counter()
    
    tiempo_total = fin - inicio
    print(f"Fibonacci({valor}) = {resultado} | Tiempo: {tiempo_total:.6f} segundos")