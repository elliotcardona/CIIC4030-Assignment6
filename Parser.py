import sys
import ply.yacc as yacc
from Lexer import tokens
import server_client

def p_start_server(p):
    'start : START_SERVER'
    print(p[1])
    server_client.execute('server')

def p_create_client_noIP(p):
    'start : START_CLIENT'
    server_client.execute('client')

def p_done(p):
    'start : FINISH'
    sys.exit(0)


def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

while True:
    try:
        s = input('S > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)