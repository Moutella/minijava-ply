import ply.yacc as yacc
import minijavalex

tokens = minijavalex.tokens


def p_prog(p):
    'prog: main classes'
    pass

def p_classes(p):
    '''
    classes: classes classe
            | classe
    '''
def p_main(p):
    'class ID LCURLY PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ID RPAREN LCURLY cmd RCURLY RCURLY'

def p_classe(p):
    '''
    classe: CLASS ID EXTENDS ID LCURLY vars metodos RCURLY
            | CLASS ID LCURLY vars metodos RCURLY
    '''
def p_vars(p):
    '''
    vars: var
        | vars var
    '''

def p_var(p):
    '''
    var: tipo ID SEMICOLON
        | ID ID SEMICOLON
    '''
def p_metodos(p):
    '''
    metodos: metodo
            | metodos metodo
    '''
def p_metodo(p):
    '''
    metodo: PUBLIC tipo ID LPARENS params RPARENS LCURLY vars cmds RETURN exp SEMICOLON RCURLY
            | PUBLIC tipo ID LPARENS RPARENS LCURLY vars cmds RETURN exp SEMICOLON RCURLY
            | PUBLIC ID ID LPARENS params RPARENS LCURLY vars cmds RETURN exp SEMICOLON | RCURLY
            | PUBLIC ID ID LPARENS RPARENS LCURLY vars cmds RETURN exp SEMICOLON RCURLY
    '''

def p_params(p):
    '''
    params: tipo ID
    | params COMMA tipo ID
    | ID ID
    |params COMMA ID ID
    '''

def p_tipo(p):
    '''
    tipo: INT LBRACKET RBRACKET
        | BOOLEAN
        | INT
    '''

def p_cmds(p):
    '''
    cmds: cmd
        | cmds cmd
    '''

def p_cmd(p):
    '''
    cmd: LCURLY cmds RCURLY
        | IF LPARENS exp RPARENS cmd
        | IF LPARENS exp RPARENS cmd ELSE cmd
        | WHILE LPARENS exp RPARENS cmd
        | PRINTLN LPARENS exp RPARENS SEMICOLON
        | ID ASSIGN exp SEMICOLON
        | ID LBRACKET exp RBRACKET ASSIGN exp SEMICOLON
    '''

def p_exp(p):
    '''
    exp: exp AND rexp
    | rexp
    '''

def p_rexp(p):
    '''
    rexp: rexp LTHAN aexp
        | rexp  EQUALS aexp
        | rexp DIFFERENT aexp
        | aexp
    '''
def p_aexp(p):
    '''
    aexp: aexp PLUS mexp
        | aexp MINUS mexp
        | mexp
    '''

def p_mexp(p):
    '''
    mexp: mexp TIMES sexp
        | sexp
    '''

def p_sexp(p):
    '''
    sexp:NOT sexp
        | MINUS sexp
        | TRUE
        | FALSE
        | NUM
        | NULL
        | NEW INT LBRACKET exp RBRACKET
        | pexp DOT LENGTH
        | ID DOT LENGTH
        | pexp LBRACKET exp RBRACKET
        | ID LBRACKET exp RBRACKET
        | ID
    '''
def p_pexp(p):
    '''
    pexp: THIS
        | NEW ID LPARENS RPARENS
        | LPARENS exp RPARENS
        | pexp DOT ID
        | ID DOT ID
        | pexp DOT ID LPARENS exps RPARENS
        | pexp DOT ID LPARENS RPARENS
        | ID DOT ID LPARENS exps RPARENS
        | ID DOT ID LPARENS RPARENS
    '''
def p_exps(p):
    '''
    exps: exps COMMA exp
        | exp
    '''
