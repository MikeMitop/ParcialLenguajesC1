%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern FILE *yyin;
int yylex(void);
void yyerror(const char *s);

/* Implementación del Método de Newton-Raphson en C */
double sqrt_newton(double n) {
    if (n < 0) {
        printf("Error: No se puede calcular la raiz de un numero negativo (%f)\n", n);
        return -1.0;
    }
    if (n == 0) return 0.0;
    
    double x = n;
    double root;
    double tolerancia = 0.000001;
    
    while (1) {
        root = 0.5 * (x + (n / x));
        /* fabs() calcula el valor absoluto en C (requiere math.h) */
        if (fabs(root - x) < tolerancia) {
            break;
        }
        x = root;
    }
    return root;
}
%}

%union {
    double val;
}

%token <val> NUMBER
%token SQRT EOL

%%
/* Gramática para procesar múltiples líneas */
calc:
    | calc expr EOL
    | calc EOL
    ;

expr:
    SQRT NUMBER { 
        double resultado = sqrt_newton($2); 
        if (resultado != -1.0) {
            printf("La raiz cuadrada de %.2f es: %f\n", $2, resultado); 
        }
    }
    ;
%%

void yyerror(const char *s) {
    fprintf(stderr, "Error de sintaxis: %s\n", s);
}

int main(int argc, char **argv) {
    // Verificar si se pasó el archivo .txt como argumento
    if (argc > 1) {
        FILE *archivo = fopen(argv[1], "r");
        if (!archivo) {
            fprintf(stderr, "No se pudo abrir el archivo: %s\n", argv[1]);
            return 1;
        }
        yyin = archivo; // Redirigir la entrada de Flex al archivo
    } else {
        printf("Por favor, proporciona un archivo .txt\n");
        printf("Uso: ./calculadora entrada.txt\n");
        return 1;
    }
    
    yyparse();
    return 0;
}