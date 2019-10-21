import sys
from minijavalex import tokens
import ply.yacc as yacc
import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()
if sys.version_info[0] >= 3:
    raw_input = input

start = 'prog'


def p_prog(p):
    'prog : main classes'
    print("\n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_main(p):
    '''
    main : CLASS ID LCURLY PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ID RPAREN LCURLY cmd RCURLY RCURLY
        | ID LCURLY PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ID RPAREN LCURLY cmd RCURLY RCURLY
    '''

    print("main \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_classes(p):
    '''
    classes : classe
            | classes classe
    '''

    print("classes \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_classe(p):
    '''
    classe : CLASS ID EXTENDS ID LCURLY vars metodos RCURLY
            | CLASS ID LCURLY vars metodos RCURLY
    '''
    print("classe \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_vars(p):
    '''
    vars : var
        | vars var
        | empty
    '''

    print("vars \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_var(p):
    '''
    var : tipo ID SEMICOLON
        | ID ID SEMICOLON
    '''
    print("var \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_metodos(p):
    '''
    metodos : metodo
            | metodos metodo
    '''
    print("metodos \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_metodo(p):
    '''
    metodo : PUBLIC tipo ID LPAREN params RPAREN LCURLY vars cmds RETURN exp SEMICOLON RCURLY
            | PUBLIC tipo ID LPAREN RPAREN LCURLY vars cmds RETURN exp SEMICOLON RCURLY
            | PUBLIC ID ID LPAREN params RPAREN LCURLY vars cmds RETURN exp SEMICOLON RCURLY
            | PUBLIC ID ID LPAREN RPAREN LCURLY vars cmds RETURN exp SEMICOLON RCURLY
            | empty
    '''

    print("metodo \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_params(p):
    '''
    params : tipo ID
    | params COMMA tipo ID
    | ID ID
    | params COMMA ID ID
    '''

    print("params \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_tipo(p):
    '''
    tipo : INT LBRACKET RBRACKET
        | BOOLEAN
        | INT
    '''

    print("tipo \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_cmds(p):
    '''
    cmds : cmd
        | cmds cmd
    '''

    print("cmds \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


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

    print("cmd \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_exp(p):
    '''
    exp : exp AND rexp
    | rexp
    '''

    print("exp \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_rexp(p):
    '''
    rexp : rexp LTHAN aexp
        | rexp  EQUALS aexp
        | rexp DIFFERENT aexp
        | aexp
    '''
    print("rexp \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_aexp(p):
    '''
    aexp : aexp PLUS mexp
        | aexp MINUS mexp
        | mexp
    '''

    print("aexp \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_mexp(p):
    '''
    mexp : mexp TIMES sexp
        | sexp
    '''

    print("mexp \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


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
    print("sexp \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


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
    print("pexp \n Stack \n {} \n Slice \n  {}".format(p.stack, p.slice))


def p_exps(p):
    '''
    exps : exp
        | exps COMMA exp
    '''

    print("exps\n Stack \n {} \n Slice \n{}".format(p.stack, p.slice))


def p_error(p):
    print("Syntax error in input! {}".format(p))

def p_empty(p):
    'empty :'
    pass


parser = yacc.yacc(debug=True, method='SLR', debuglog=log, errorlog=log)
sourcefile = open('minijava-ply/example.minijava', "r")
code = sourcefile.readlines()
codetxt = ''
for line in code:
    codetxt += line

try:
    s = codetxt
except EOFError:
    print('Cabo')
if not s:
    pass
result = parser.parse(s, debug=log)
print(result)
