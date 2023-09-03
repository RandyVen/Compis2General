grammar YAPL;
program : 
   programBlock EOF
   ;
programBlock:
   classDEF ';' programBlock
   | EOF
   ;
classDEF : 
    CLASS TYPEID (INHERITS TYPEID)? '{' (feature ';')* '}';
feature : 
    (OBJECTID) '(' (formal (','formal)*)? ')' ':' TYPEID '{' expr '}' #MethodDef
    | OBJECTID ':' TYPEID (ASIGNOPP expr)? #FeactureDecalration
    ;
formal:
    OBJECTID ':' TYPEID;
expr :
    expr ('@' TYPEID)? '.' OBJECTID '(' (expr (',' expr)*)? ')' #MethodExpr 
    | OBJECTID '(' (expr (',' expr)*)? ')' #FunctionExpr
    | IF expr THEN expr ELSE expr FI #ifElseExpr
    | WHILE expr LOOP expr POOL #whileExpr
    | '{' (expr ';')* '}' #BraketedExpr
    | 'let' OBJECTID ':' TYPEID (ASIGNOPP expr)? (',' OBJECTID ':' TYPEID (ASIGNOPP expr)?)* IN expr #letExpr
    | NEW TYPEID #newExpr 
    | ISVOID expr #isVoidExpr
    | expr '*' expr #multiplyExpr
    | expr '/' expr #divideExpr
    | expr '+' expr #addExpr
    | expr '-' expr #substractExpr
    | '~' expr #neggateExpr
    | expr '<' expr #lessExpr
    | expr '<=' expr #lessEqualExpr
    | expr '=' expr #equalExpr
    | NOT expr #notExpr
    | '(' expr ')' #parenthExpr
    | OBJECTID #objectIdExpr
    | INTEGERS #integerExpr
    | STRINGS #stringExpr
    | TRUE #trueExpr
    | FALSE #falseExpr
    | OBJECTID ASIGNOPP expr #DeclarationExpression
    ;
//Palabras reservadas
CLASS
   : C L A S S
   ;

ELSE
   : E L S E
   ;

FALSE
   : 'false'
   ;

FI
   : F I
   ;

IF
   : I F
   ;

IN
   : I N
   ;

INHERITS
   : I N H E R I T S
   ;

ISVOID
   : I S V O I D
   ;

LET
   : L E T
   ;

LOOP
   : L O O P
   ;

POOL
   : P O O L
   ;

THEN
   : T H E N
   ;

WHILE
   : W H I L E
   ;

NEW
   : N E W
   ;

NOT
   : N O T
   ;

TRUE
   : 'true'
   ;

//Tipos primitivos

STRINGS
   : '"' (ESC | ~ ["\\])* '"'
   ;
INTEGERS
   : [0-9]+
   ;
TYPEID
   : [A-Z] [_0-9A-Za-z]*
   ;
OBJECTID
   : [a-z] [_0-9A-Za-z]*
   ;
ASIGNOPP
    : '<-'
    ;
fragment A
   : [aA]
   ;
fragment C
   : [cC]
   ;
fragment D
   : [dD]
   ;
fragment E
   : [eE]
   ;
fragment F
   : [fF]
   ;
fragment H
   : [hH]
   ;
fragment I
   : [iI]
   ;
fragment L
   : [lL]
   ;
fragment N
   : [nN]
   ;
fragment O
   : [oO]
   ;
fragment P
   : [pP]
   ;
fragment R
   : [rR]
   ;
fragment S
   : [sS]
   ;
fragment T
   : [tT]
   ;
fragment U
   : [uU]
   ;
fragment V
   : [vV]
   ;
fragment W
   : [wW]
   ;
fragment ESC
   : '\\' (["\\/bfnrt] | UNICODE)
   ;
fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;
fragment HEX
   : [0-9a-fA-F]
   ;
// Comentarios y espacios en blanco 
   
OPEN_COMMENT
   : '(*'
   ;
CLOSE_COMMENT
   : '*)'
   ;
COMMENT
   : OPEN_COMMENT (COMMENT | .)*? CLOSE_COMMENT -> skip
   ;
ONE_LINE_COMMENT
   : '--' (~ '\n')* '\n'? -> skip
   ;

WHITESPACE
   : [ \t\r\n\f]+ -> skip
   ;
   