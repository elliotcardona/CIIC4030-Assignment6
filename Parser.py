import ply.yacc as yacc
from Lexer import tokens
import server

def p_start_server(p):
    'start : START_SERVER'
    print(p[1])
    server.run('server')

def p_create_client_noIP(p):
    'start : START_CLIENT'
    print('Client')
    server.run('client')

def p_creat_client(p):
    'start : START_CLIENT IP'
    print('Client ip')
    server.p2p.peers = p[2]
    server.run('client')



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