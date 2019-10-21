import ply.lex as lex

reserved = {
    'boolean': 'BOOLEAN',
    'class': 'CLASS',
    'extends': 'EXTENDS',
    'public': 'PUBLIC',
    'static': 'STATIC',
    'void': 'VOID',
    'main': 'MAIN',
    'String': 'STRING',
    'return': 'RETURN',
    'int': 'INT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'System.out.println': 'PRINTLN',
    'length': 'LENGTH',
    'true': 'TRUE',
    'false': 'FALSE',
    'this': 'THIS',
    'new': 'NEW',
    'null': 'NULL'
}

tokens = [
    'WS',
    'COMMENT',
    'ID',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LCURLY',
    'RCURLY',
    'SEMICOLON',
    'DOT',
    'COMMA',
    'GEQUAL',
    'LEQUAL',
    'EQUALS',
    'DIFFERENT',
    'ASSIGN',
    'LTHAN',
    'GTHAN',
    'PLUS',
    'MINUS',
    'TIMES',
    'AND',
    'NOT'
] + list(reserved.values())

t_ignore_MULTICOMMENT = r'(\/\*[^\n]*\*\/)'
t_ignore_COMMENT = r'\/\/.*'
t_ignore_WS = r'[ \n\t\r\f]'
t_ID = r'[a-zA-Z][a-zA-Z0-9_]*'
t_NUMBER = r'[0-9]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_SEMICOLON = r';'
t_DOT = r'\.'
t_COMMA = r','
t_GEQUAL = r'>='
t_LEQUAL = r'<='
t_EQUALS = r'=='
t_DIFFERENT = r'!='
t_ASSIGN = r'='
t_LTHAN = r'<'
t_GTHAN = r'>'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_AND = r'&&'
t_NOT = r'!'

#
#def t_NUMBER(t):
#    r'[0-9]+'
#    t.value = int(t.value)
#    return t
#
#
#def t_ID(t):
#    r'[a-zA-Z][a-zA-Z0-9_]*'
#    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
#    return t
#
#
#def t_newline(t):
#    r'\n+'
#    t.lexer.lineno += len(t.value)
#
#
#def t_error(t):
#    print("Illegal character '%s'" % t.value[0])
#    t.lexer.skip(1)
#
#
lexer = lex.lex()

sourcefile = open('example.minijava', "r")
code = sourcefile.readlines()
codetxt = ''
for line in code:
    codetxt += line

lexer.input(codetxt)

while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
