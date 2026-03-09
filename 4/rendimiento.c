#include <stdio.h>
#include <time.h>

long long fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int valores[] = {10, 20, 30, 40}; 
    int num_valores = sizeof(valores) / sizeof(valores[0]);
    double tiempos[num_valores];

    printf("Comparacion de rendimiento en C (Compilado)\n");
    for (int i = 0; i < num_valores; i++) {
        clock_t inicio = clock();
        long long resultado = fibonacci(valores[i]);
        clock_t fin = clock();

        tiempos[i] = (double)(fin - inicio) / CLOCKS_PER_SEC;
        printf("Fibonacci(%d) = %lld | Tiempo: %f segundos\n", valores[i], resultado, tiempos[i]);
    }
    return 0;
}