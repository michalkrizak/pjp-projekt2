grammar PJP;

prog: statement* EOF;

statement
        :   ';'                                                 #EmptyCommandStat
        |   varType VAR (',' VAR)* ';'                             #DeclarationStat
        |   expression ';'                                      #ExpressionStat
        |   'read' VAR (',' VAR)* ';'                           #ReadStat
        |   'write' expression (',' expression)* ';'            #WriteStat
        |   '{' statement* '}'                                  #StatementStat
        |   'if' '(' expression ')' statement ('else' statement)?    #IfStat
        |   'while' '(' expression ')' statement                #WhileStat
        |   'do' statement 'while' '(' expression ')' ';'      #DoWhileStat
        |   'for' '(' expression ';' expression ';' expression ')' statement  #ForStat
        |   'fopen' VAR STRING ';'                              #FopenStat
        |   'fwrite' VAR (',' expression)+ ';'                  #FwriteStat
        |   'fappend' VAR (',' expression)+ ';'                 #FappendStat
        |   VAR ('<<' expression)+ ';'                          #FileStreamStat
        ;

varType
    :   'int'
    |   'float'
    |   'bool'
    |   'string'
    |   'FILE'
    ;

expression
        :   '-' expression                              #UnaryMinusExpr
        |   '!' expression                              #LogicNotExpr     
        |   expression op=('*'|'/'|'%') expression      #MultDivModExpr
        |   expression op=('+'|'-'|'.') expression      #PlusMinusConcatExpr
        |   expression op=('<'|'>') expression                      #HigherLowerExpr
        |   expression op=('=='|'!=') expression                    #EqualNotEqualExpr
        |   expression '&&' expression                              #AndExpr
        |   expression '||' expression                              #OrExpr
        |   VAR '=' expression                                #AssignExpr
        |   'charAt' '(' expression ',' expression ')'        #CharAtExpr
        |   'len' '(' expression ')'                          #LenExpr
        |   '(' expression ')'                                #ParenExpr
        |   INT                                         #IntExpr
        |   FLOAT                                       #FloatExpr
        |   BOOL                                        #BoolExpr
        |   STRING                                      #StringExpr
        |   VAR                                         #VarExpr
        ;

FLOAT   : [0-9]+ '.' [0-9]* ;
INT     : [0-9]+ ;
BOOL    : 'true' | 'false' ;
STRING  : '"' (~["\r\n])* '"' ;
VAR      : [a-zA-Z][a-zA-Z0-9]* ;
COMMENT : '//' ~[\r\n]* -> skip ;
WS      : [ \t\r\n]+ -> skip ;
            


    