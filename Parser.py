import sys
import ply.yacc as yacc
from Lexer import tokens
import server_client


def p_start_server(p):
    'start : START_SERVER'
    print(p[1])
    server_client.execute('server')

def p_set_anonymity(p):
    'start : ANONYMITY ID'
    if p[2].lower()=="true":
        server_client.setAnonymity(True)
        print("Anonymity changed to:", server_client.getAnonymity())
    elif p[2].lower()=="false":
        server_client.setAnonymity(False)
        print("Anonymity changed to:", server_client.getAnonymity())
    else:
        print("Not a valid argument. Must be a bool \"true\" or \"false\".")

def p_start_server_wArgs(p):
    'start : START_SERVER NUMBER ID'
    if p[3].lower()=="true":
        server_client.setAnonymity(True)
        print("Anonymity changed to:", server_client.getAnonymity())
    elif p[3].lower()=="false":
        server_client.setAnonymity(False)
        print("Anonymity changed to:", server_client.getAnonymity())
    else:
        print("Not a valid argument. Must be a bool \"true\" or \"false\".")

    server_client.setServerPort(p[2])
    print("Server Port Changed to:",server_client.getServerPort())
    print(p[1])
    server_client.execute('server')

def p_start_client_wArgs(p):
    'start : START_CLIENT NUMBER'
    server_client.setClientPort(p[2])
    print("Client Port Changed to:",server_client.getClientPort())
    server_client.execute('client')

def p_set_server_port(p):
    'start : SET_SERVER_PORT NUMBER'
    server_client.setServerPort(p[2])
    print("Server Port Changed to:",server_client.getServerPort())

def p_set_client_port(p):
    'start : SET_CLIENT_PORT NUMBER'
    server_client.setClientPort(p[2])
    print("Client Port Changed to:",server_client.getClientPort())

def p_get_server_port(p):
    'start : GET_SERVER_PORT'
    print(server_client.getServerPort())

def p_get_client_port(p):
    'start : GET_CLIENT_PORT'
    print(server_client.getClientPort())

def p_create_client_noIP(p):
    'start : START_CLIENT'
    server_client.execute('client')

def p_done(p):
    'start : FINISH'
    sys.exit(0)


def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()
