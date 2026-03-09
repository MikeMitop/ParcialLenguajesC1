%{
#include "calculadora.tab.h"
#include <stdlib.h>
%}

%%
[-]?[0-9]+(\.[0-9]+)?   { yylval.val = atof(yytext); return NUMBER; }
"SQRT"|"sqrt"       { return SQRT; }
[ \t]+              { /* Ignorar espacios y tabulaciones */ }
\n                  { return EOL; }
.                   { /* Ignorar otros caracteres no reconocidos */ }
%%

int yywrap() { 
    return 1; 
}