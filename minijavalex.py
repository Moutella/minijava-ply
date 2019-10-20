import ply.lex as lex
reserved = {
    'boolean': 'BOOLEAN'
    'class': 'CLASS'
    'extends': 'EXTENDS'
    'public': 'PUBLIC'
    'static': 'STATIC'
    'void': 'VOID'
    'main': 'MAIN'
    'String': 'STRING'
    'return': 'RETURN'
    'int': 'INT'
    'if': 'IF'
    'else': 'ELSE'
    'while': 'WHILE'
    'System.out.println': 'PRINTLN'
    'length': 'LENGTH'
    'true': 'TRUE'
    'false': 'FALSE'
    'this': 'THIS'
    'new': 'NEW'
    'null': 'NULL'
}

tokens = [
    'WS',
    'COMMENT',
    'ID',
    'NUMBER',
    'LPAREN',
    'RPAREN', 
    'LBRACKET', #[
    'RBRACKET', #]
    'LCURLY', #{
    'RCURLY', #}
    'SEMICOLON', #;
    'DOT',
    'COMMA',
    'ASSIGN', #=
    'LTHAN',
    'GTHAN',
    'GEQUAL',
    'LEQUAL',
    'EQUALS', #==
    'DIFFERENT', #!=,
    'PLUS',
    'MINUS',
    'TIMES',
    'AND', #&&
    'NOT' #!
] + reserved