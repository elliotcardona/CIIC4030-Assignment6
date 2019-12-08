import ply.yacc as yacc
from Lexer import tokens
import server

def p_start_server(p):
    'start : START_SERVER'
    print(p[1])
    server.run()

def p_start_client(p):
    'start : START_CLIENT IP'
    server.p2p.peers = p[2]
    server.run()


def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)