import ply.yacc as yacc
import minijavalex

tokens = minijavalex.tokens


def p_program(p):
    'program: main LCURLY class RCURLY'
    pass

def p_main(p):
    'class ID LCURLY PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ID RPAREN LCURLY cmd RCURLY RCURLY'

