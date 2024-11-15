grammar Python;

prog: (conditional | assignment)* | EOF;

assignment: (IDENTIFIER  ASSIGN_OP  value);

IF: 'if';

ELIF: 'elif';

ELSE: 'else';

conditional: IF boolean_expr ':' ('\t' assignment)* cond_elif* cond_else?;

cond_elif: ELIF boolean_expr ':' ('\t' assignment)*;

cond_else: ELSE ('\t' assignment)*;

boolean_expr: boolean_expr AND_OR boolean_expr | NOT boolean_expr | expr COMPARE_OP expr | expr | '(' boolean_expr ')';

COMPARE_OP: '>' | '<' | '>' '=' | '<' '=' | '=' '=' | '!' '=';

AND_OR: 'a''n''d' | 'o''r';

NOT: 'n''o''t';

WS: [ \r\n]+ -> skip;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

ASSIGN_OP: '=' | '+''=' | '-''=' | '*''=' | '/''=';

value: LITERAL | expr | IDENTIFIER;

LITERAL: STR_LIT | INT_LIT | FLOAT_LIT | LIST_LIT | BOOLEAN_LIT;

STR_LIT: '"' [a-zA-Z0-9 ]* '"' | '\'' [a-zA-Z0-9]* '\'';

INT_LIT: [0-9]+ | '-' [0-9]+;

FLOAT_LIT: [0-9]+ '.' [0-9]+ | '-' [0-9]+ '.' [0-9]+;

LIST_LIT: '['  LIST_ELEMENT*  ']';

LIST_ELEMENT: LITERAL (',' WS LIST_ELEMENT)*;

BOOLEAN_LIT: 'T''r''u''e' | 'F''a''l''s''e';

expr: LITERAL | IDENTIFIER | expr  ARITH_OP  expr;

ARITH_OP: '+' | '-' | '*' | '/' | '%';