grammar PJP;

prog: statement* EOF;

statement
        :   ';'                                                 #EmptyCommandStat
        |   varType VAR '[' INT ']' ';'                         #ArrayDeclStat
        |   varType VAR (',' VAR)* ';'                             #DeclarationStat
        |   expression ';'                                      #ExpressionStat
        |   'read' VAR (',' VAR)* ';'                           #ReadStat
        |   'write' expression (',' expression)* ';'            #WriteStat
        |   '{' statement* '}'                                  #StatementStat   
        |   'if' '(' expression ')' statement ('else' statement)?    #IfStat
        |   'while' '(' expression ')' statement                #WhileStat
        ;

varType
    :   'int'
    |   'float'
    |   'bool'
    |   'string'
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
        |   VAR '[' expression ']' '=' expression              #ArrayAssignExpr
        |   VAR '=' expression                                #AssignExpr
        |   VAR '[' expression ']'                            #ArrayAccessExpr
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
            


    