grammar Fibonacci;

// Regla inicial
prog: fibo EOF ;

// Reconoce FIBO(numero)
fibo: 'FIBO' '(' NUM ')' ;

// Token número
NUM: [0-9]+ ;

// Ignorar espacios
WS: [ \t\r\n]+ -> skip ;
