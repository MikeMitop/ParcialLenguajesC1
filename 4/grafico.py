import matplotlib.pyplot as plt

valores_c = [10, 20, 30, 40]
tiempos_c = [0.000004, 0.000100, 0.013057, 1.207690]

valores_py = [10, 20, 30]
tiempos_py = [0.000017, 0.001414, 0.130027]

plt.figure(figsize=(10, 6))

plt.plot(valores_c, tiempos_c, marker='o', label='C (Compilado)', color='#1f77b4', linewidth=2.5, markersize=8)
plt.plot(valores_py, tiempos_py, marker='s', label='Python (Interpretado)', color='#ff7f0e', linewidth=2.5, markersize=8)

for i, txt in enumerate(tiempos_c):
    plt.annotate(f"{txt:.6f}s", (valores_c[i], tiempos_c[i]), 
                 textcoords="offset points", xytext=(0,-15), ha='center', fontsize=9, color='#1f77b4')

for i, txt in enumerate(tiempos_py):
    plt.annotate(f"{txt:.6f}s", (valores_py[i], tiempos_py[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='#ff7f0e')

plt.title('Comparación de Rendimiento: C vs Python\n(Sucesión de Fibonacci Recursiva)', fontsize=15, pad=15)
plt.xlabel('N (Valor a calcular de Fibonacci)', fontsize=12)
plt.ylabel('Tiempo de ejecución (Segundos)', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks([10, 20, 30, 40])
plt.tight_layout()

plt.savefig('grafica_rendimiento.png')
