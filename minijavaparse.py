import sys
from minijavalex import tokens
from symbol_table import *
import ply.yacc as yacc
import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()
if sys.version_info[0] >= 3:
    raw_input = input

start = 'prog'


def p_prog(p):
    'prog : main classes'
    p[0] = (p[0], p[1], p[2], p.lineno(0))


def p_main(p):
    '''
    main : CLASS ID LCURLY PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ID RPAREN LCURLY cmd RCURLY RCURLY
    '''
    add_symbol_to_scope(p[2])
    p[0] = ('main', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8],
            p[9], p[10], p[11], p[12], p[13], p[14], p[15], p[16], p[17], p.lineno(0))


def p_classes(p):
    '''
    classes : classe
            | classes classe
    '''

    if(len(p) == 3):
        p[0] = ('classes', p[1], p[2], p.lineno(0))
    else:
        p[0] = ('classes', p[1], p.lineno(0))
    


def p_classe(p):
    '''
    classe : CLASS ID EXTENDS ID LCURLY vars metodos RCURLY
            | CLASS ID LCURLY vars metodos RCURLY
            | empty
    '''
    if(len(p) == 9):
        add_symbol_to_scope(p[2])
        add_symbol_to_dependencies(p[4], p.lineno(4))
        p[0] = ('classe', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p.lineno(0))
    elif(len(p) == 7):
        add_symbol_to_scope(p[2])
        p[0] = ('classe', p[1], p[2], p[3], p[4], p[5], p[6], p.lineno(0))
    else:
        p[0] = ('classe', p.lineno(0))
    


def p_vars(p):
    '''
    vars : var
        | vars var
        | empty
    '''

    if(len(p) == 2):
        if(p[1]):
            p[0] = ('vars', p[1], p.lineno(0))
        else:
            p[0] = ('vars', p.lineno(0))
    elif(len(p)==3):
        p[0] = ('vars', p[1], p[2], p.lineno(0))


def p_var(p):
    '''
    var : tipo ID SEMICOLON
        | ID ID SEMICOLON
    '''
    p[0] = ('var',p[1],p[2],p[3], p.lineno(0))

def p_metodos(p):
    '''
    metodos : metodo
            | metodos metodo
    '''
    if(len(p) == 2):
        p[0] = ('metodos', p[1], p.lineno(0))
    else:
        p[0] = ('metodos', p[1], p[2], p.lineno(0))
    


def p_metodo(p):
    '''
    metodo : PUBLIC tipo ID LPAREN params RPAREN LCURLY vars cmds RETURN exp SEMICOLON RCURLY
            | PUBLIC tipo ID LPAREN RPAREN LCURLY vars cmds RETURN exp SEMICOLON RCURLY
            | PUBLIC ID ID LPAREN params RPAREN LCURLY vars cmds RETURN exp SEMICOLON RCURLY
            | PUBLIC ID ID LPAREN RPAREN LCURLY vars cmds RETURN exp SEMICOLON RCURLY
            | empty
    '''
    if(len(p)==14):
            p[0] = ('metodo', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8],
            p[9], p[10], p[11], p[12], p[13], p.lineno(0))
    if(len(p)==13):
            p[0] = ('metodo', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8],
            p[9], p[10], p[11], p[12], p.lineno(0))
    else:
        p[0] = ('metodo', p.lineno(0))
    


def p_params(p):
    '''
    params : tipo ID
    | params COMMA tipo ID
    | ID ID
    | params COMMA ID ID
    '''
    if len(p) == 3:
        p[0] = ('params', p[1], p[2], p.lineno(0))
    else:
        p[0] = ('params', p[1], p[2], p[3], p[4], p[5], p.lineno(0))


def p_tipo(p):
    '''
    tipo : INT LBRACKET RBRACKET
        | BOOLEAN
        | INT
    '''

    if len(p) == 4:
        p[0] = ('tipo', p[1], p[2], p[3], p.lineno(0))
    else:
        p[0] = ('tipo', p[1], p.lineno(0))


def p_cmds(p):
    '''
    cmds : cmd
        | cmds cmd
    '''
    if len(p) == 2:
        p[0] = ('cmds', p[1], p.lineno(0))
    else:
        p[0] = ('cmds', p[1], p[2], p.lineno(0))


def p_cmd(p):
    '''
    cmd : LCURLY cmds RCURLY    
        | IF LPAREN exp RPAREN cmd
        | IF LPAREN exp RPAREN cmd ELSE cmd
        | WHILE LPAREN exp RPAREN cmd
        | PRINTLN LPAREN exp RPAREN SEMICOLON
        | ID ASSIGN exp SEMICOLON
        | ID LBRACKET exp RBRACKET ASSIGN exp SEMICOLON
        | empty
    '''
    if len(p) == 8:
        p[0] = ('cmd', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p.lineno(0))
    elif len(p) == 6:
        p[0] = ('cmd', p[1], p[2], p[3], p[4], p[5], p.lineno(0))
    elif len(p) == 5:
        p[0] = ('cmd', p[1], p[2], p[3], p[4], p.lineno(0))
    else:
        p[0] = ('cmd', p.lineno(0))

def p_exp(p):
    '''
    exp : exp AND rexp
    | rexp
    '''
    if len(p) == 4:
        p[0] = ('exp', p[1], p[2], p[3], p.lineno(0))
    else:
        p[0] = ('exp', p[1], p.lineno(0))


def p_rexp(p):
    '''
    rexp : rexp LTHAN aexp
        | rexp  EQUALS aexp
        | rexp DIFFERENT aexp
        | aexp
    '''
    if len(p) == 4:
        p[0] = ('rexp', p[1], p[2], p[3], p.lineno(0))
        # if type(p[1]) == type (p[3]) == int:
        #     if p[2] == "<":
        #         p[0] = p[1] + p[3]
        #     elif p[2] == "==":
        #         pass
        #     elif p[2]== "!=":
        #         p[0] = p[1] - p[3]
    else:
        if type(p[1]) == int:
            p[0] = p[1]
        else:
            p[0] = ('rexp', p[1], p.lineno(0))

def p_aexp(p):
    '''
    aexp : aexp PLUS mexp
        | aexp MINUS mexp
        | mexp
    '''
    if len(p) == 4:
        print("aexp: {} {} {}".format(p[1], p[2], p[3]))
        if type(p[1]) == type (p[3]) == int:
            if p[2] == "+":
                p[0] = p[1] + p[3]
            else:
                p[0] = p[1] - p[3]
        else:
            p[0] = ('aexp', p[1], p[2], p[3], p.lineno(0))
    else:
        if type(p[1]) == int:
            p[0] = p[1]
        else:
            p[0] = ('aexp', p[1], p.lineno(0))


def p_mexp(p):
    '''
    mexp : mexp TIMES sexp
        | sexp
    '''
    
    if len(p) == 4:
        print("mexp: {} {} {}".format(p[1], p[2], p[3]))
        if type(p[1]) == type(p[3]) == int:
            p[0] = p[1] * p[3]
        else:
            p[0] = ('mexp', p[1], p[2], p[3], p.lineno(0))
    else:
        print("mexp: {}".format( p[1]))
        if type(p[1]) == int:
            p[0] = p[1]
        else:
            p[0] = ('mexp', p[1], p.lineno(0))

def p_sexp(p):
    '''
    sexp : NOT sexp
        | MINUS sexp
        | TRUE
        | FALSE
        | NUMBER
        | NULL
        | NEW INT LBRACKET exp RBRACKET
        | pexp DOT LENGTH
        | ID DOT LENGTH
        | pexp LBRACKET exp RBRACKET
        | ID LBRACKET exp RBRACKET
        | ID
        | pexp
    '''
    if len(p) == 6:
        p[0] = ('sexp', p[1], p[2], p[3], p[4], p[5], p.lineno(0))
    elif len(p) == 5:
        p[0] = ('sexp', p[1], p[2], p[3], p[4], p.lineno(0))
    elif len(p) == 4:
        p[0] = ('sexp', p[1], p[2], p[3], p.lineno(0))
    elif len(p) == 3:
        p[0] = ('sexp', p[1], p[2], p.lineno(0))
    else:
        if type(p[1]) == int:
            p[0] = p[1]
        else:
            p[0] = ('sexp', p[1], p.lineno(0))


def p_pexp(p):
    '''
    pexp : THIS
        | NEW ID LPAREN RPAREN
        | LPAREN exp RPAREN
        | pexp DOT ID
        | ID DOT ID
        | pexp DOT ID LPAREN exps RPAREN
        | pexp DOT ID LPAREN RPAREN
        | ID DOT ID LPAREN exps RPAREN
        | ID DOT ID LPAREN RPAREN
    '''
    result = ()
    result += 'pexp',
    for s in p[1:]:
        result += (s,)
    result += p.lineno(0),
    p[0] = result
    
    
def p_exps(p):
    '''
    exps : exp
        | exps COMMA exp
    '''
    result = ()
    result += 'exps',
    for s in p[1:]:
        result += (s,)
    result += p.lineno(0),
    p[0] = result
    


def p_error(p):
    if p:
        print("Erro de sintace no token: {}".format(p))
        parser.errok()
    else:
        print("Erro de sintaxe com EOF")

def p_empty(p):
    'empty :'
    pass


parser = yacc.yacc(debug=True, method='SLR', debuglog=log, errorlog=log)
sourcefile = open('example.minijava', "r")
code = sourcefile.readlines()
codetxt = ''
for line in code:
    codetxt += line

try:
    s = codetxt
except EOFError:
    print("Erro EOF")
if not s:
    pass



result = parser.parse(s, tracking=True, debug=log)