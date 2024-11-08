grammar Python;

prog: assignment* | EOF;

assignment: (IDENTIFIER  ASSIGN_OP  value);

WS: [ \r\n]+ -> skip;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

ASSIGN_OP: '=' | '+''=' | '-''=' | '*''=' | '/''=';

value: LITERAL | expr | IDENTIFIER;

LITERAL: STR_LIT | INT_LIT | FLOAT_LIT | LIST_LIT | BOOLEAN_LIT;

STR_LIT: '"' [a-zA-Z0-9]* '"' | '\'' [a-zA-Z0-9]* '\'';

INT_LIT: [0-9]+ | '-' [0-9]+;

FLOAT_LIT: [0-9]+ '.' [0-9]+ | '-' [0-9]+ '.' [0-9]+;

LIST_LIT: '['  LIST_ELEMENT*  ']';

LIST_ELEMENT: LITERAL (',' WS LIST_ELEMENT)*;

BOOLEAN_LIT: 'T''r''u''e' | 'F''a''l''s''e';

expr: LITERAL | IDENTIFIER | expr  ARITH_OP  expr;

ARITH_OP: '+' | '-' | '*' | '/' | '%';