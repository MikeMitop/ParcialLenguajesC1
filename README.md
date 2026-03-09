#  **Parcial 1: Lenguajes de Programación**

Miguel Ángel Celis López  
Lenguajes de Programación  
Joaquin Fernando Sanchez  
Universidad Sergio Arboleda  
2026, Bogotá DC

## **Punto 1 y 2: Autómatas Finitos Deterministas (AFD)**

Se implementaron dos scripts en Python para evaluar expresiones regulares mediante máquinas de estados, leyendo los casos de prueba desde archivos de texto.

* **Punto 1 (Movimientos de Ajedrez):** 

Implementación de un AFD para evaluar el lenguaje de movimientos como p-\>k4 o kbp X qn. La máquina de estados controla la presencia de piezas, transiciones válidas (-\> o X) y casillas de destino.

* **Punto 2 (Identificadores):**

 Implementación de un AFD para la expresión regular \[A-Za-z\]\[A-Za-z0-9\]\*, aceptando variables que inicien con letras y rechazando aquellas que inicien con números o contengan caracteres especiales (como \_).

## **Punto 3: Calculadora de Raíz Cuadrada (Flex, Bison y C)**

Se construyó una calculadora léxico-sintáctica capaz de extraer raíces cuadradas de números reales iterando desde un archivo .txt.

* **Lexer (Flex):** Atrapa la palabra reservada SQRT o sqrt y detecta números reales (incluyendo negativos para el manejo de errores).  
* **Parser (Bison):** Define la gramática y hace el llamado a la función en C.  
* **Lógica (C):** Implementa el método numérico de Newton-Raphson para aproximar la raíz cuadrada mediante la fórmula iterativa, manejando adecuadamente el rechazo de raíces negativas.

## **Punto 4: Comparación de Rendimiento (Compilado vs Interpretado)**

Se realizó una comparativa de rendimiento ejecutando la función recursiva de Fibonacci en dos lenguajes distintos.

* **Lenguaje Compilado (C):** Demostró una ejecución veloz (\~1.2 segundos para N=40) gracias a la traducción directa a código máquina.  
* **Lenguaje Interpretado (Python):** Demostró la sobrecarga del intérprete al gestionar los marcos de llamadas en tiempo real, colapsando exponencialmente en la recursividad.

*Se incluye en la entrega una gráfica generada en Python (matplotlib) evidenciando la curva de rendimiento entre ambos.*

## **Punto 5: Secuencia de Fibonacci con ANTLR**

Este proyecto implementa un programa que calcula la secuencia de Fibonacci utilizando **ANTLR4** con **Python como lenguaje objetivo**. El programa recibe una entrada y genera en consola los primeros n números de la secuencia.

### **Requisitos**

Para ejecutar el analizador se necesita:

* Python 3  
* ANTLR4  
* Runtime de ANTLR para Python

Instalación en Linux (Fedora/Ubuntu/Kali):  
sudo apt install antlr4  
pip3 install antlr4-python3-runtime

### **Generación del Parser**

El parser fue generado a partir del archivo Fibonacci.g4 (el cual define la estructura FIBO(numero)). Se ejecutó el siguiente comando en la terminal para generar los Lexers y Visitors:  
antlr4 \-Dlanguage=Python3 \-visitor Fibonacci.g4

### **Ejecución del Programa**

Para ejecutar el programa final y evaluar una cadena, se utiliza:  
python3 main.py

**Ejemplo de ejecución en consola:**  
Ingrese la expresión (ej: FIBO(8)):  
FIBO(8)  
0, 1, 1, 2, 3, 5, 8, 13

### **Explicación del funcionamiento interno (Punto 5\)**

1. **main.py:** Captura la entrada del usuario y la convierte en un InputStream que es procesado por ANTLR.  
2. **Lexer y Parser:** FibonacciLexer divide la entrada (FIBO, (, 8, )) en tokens. FibonacciParser construye el árbol sintáctico asegurando que cumple las reglas gramaticales.  
3. **Visitor (FibonacciVisitorImpl.py):** Recorre el árbol generado. Al llegar al nodo numérico, extrae el valor n, ejecuta un bucle iterativo de Python para calcular los n valores de la secuencia de Fibonacci y los imprime separados por comas.
