grammar YAPL;

start : program EOF
      ;

program: classExpr ';' program | EOF
      ;

classExpr : CLASS TYPE (INHERITS TYPE)? '{' (feature ';')* '}'
      ;

feature : (ID) '(' (formal (','formal)*)? ')' ':' TYPE '{' expr '}'                      #method
      | ID ':' TYPE (ASIGNOPP expr)?                                                     #attribute
      ;

formal:
      ID ':' TYPE
      ;

expr :
      expr ('@' TYPE)? '.' ID '(' (expr (',' expr)*)? ')'                                #dispatch 
      | ID '(' (expr (',' expr)*)? ')'                                                   #function
      | IF expr THEN expr ELSE expr FI                                                   #ifElse
      | WHILE expr LOOP expr POOL                                                        #while
      | '{' (expr ';')* '}'                                                              #bracket
      | 'let' ID ':' TYPE (ASIGNOPP expr)? (',' ID ':' TYPE (ASIGNOPP expr)?)* IN expr   #let
      | NEW TYPE                                                                         #new
      | ISVOID expr                                                                      #isVoid
      | expr MULT expr                                                                   #multiply
      | expr DIV expr                                                                    #divide
      | expr ADD expr                                                                    #add
      | expr MINUS expr                                                                  #substract
      | '~' expr                                                                         #negation
      | expr LT expr                                                                     #lessThan
      | expr LE expr                                                                     #lessEqual
      | expr EQ expr                                                                     #equal
      | NOT expr                                                                         #not
      | '(' expr ')'                                                                     #parenthesis
      | ID                                                                               #id
      | INTEGERS                                                                         #integer
      | STRINGS                                                                          #string
      | TRUE                                                                             #true
      | FALSE                                                                            #false
      | ID ASIGNOPP expr                                                                 #assignment
      ;

CLASS : C L A S S ;
INHERITS : I N H E R I T S ;
TRUE : 'true' ;
FALSE : 'false' ;
IF : I F ;
ELSE : E L S E ;
THEN : T H E N ;
FI : F I ;
WHILE : W H I L E ;
LOOP : L O O P ;
POOL : P O O L ;
LET : L E T ;
IN : I N ;
NEW : N E W ;
ISVOID : I S V O I D ;
ADD : '+' ;
MINUS : '-' ;
MULT : '*' ;
DIV : '/' ;
LT : '<' ; 
LE : '<=' ;
EQ : '=' ;
NOT : N O T ;
STRINGS : '"' (ESC | ~ ["\\])* '"' ;
INTEGERS : [0-9]+ ;
TYPE : [A-Z] [_0-9A-Za-z]* ;
ID : [a-z] [_0-9A-Za-z]* ;
ASIGNOPP : '<-' ;
WHITESPACE : [ \t\r\n\f]+ -> skip ;
fragment A : [aA] ;
fragment C : [cC] ;
fragment D : [dD] ;
fragment E : [eE] ;
fragment F : [fF] ;
fragment H : [hH] ;
fragment I : [iI] ;
fragment L : [lL] ;
fragment N : [nN] ;
fragment O : [oO] ;
fragment P : [pP] ;
fragment R : [rR] ;
fragment S : [sS] ;
fragment T : [tT] ;
fragment U : [uU] ;
fragment V : [vV] ;
fragment W : [wW] ;
fragment X : [xX] ;
fragment Y : [yY] ;
fragment Z : [zZ] ;
fragment HEX : [0-9a-fA-F] ;
fragment UNICODE : 'u' HEX HEX HEX HEX ;
fragment ESC : '\\' (["\\/bfnrt] | UNICODE) ;

OPEN_COMMENT : '(*' ;
CLOSE_COMMENT : '*)' ;
COMMENT : OPEN_COMMENT (COMMENT | .)*? CLOSE_COMMENT -> skip ;
ONE_LINE_COMMENT : '--' (~ '\n')* '\n'? -> skip ;