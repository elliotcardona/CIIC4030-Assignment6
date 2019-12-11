import ply.lex as lex

tokens = [
    'NUMBER',
    'PERIOD',
    'ID'
]

reserved = {

    'START_SERVER' : 'START_SERVER',
    'START_CLIENT' : 'START_CLIENT',
    'FINISH' : 'FINISH',
    'SET_SERVER_PORT' : 'SET_SERVER_PORT',
    'SET_CLIENT_PORT' : 'SET_CLIENT_PORT',
    'GET_SERVER_PORT' : 'GET_SERVER_PORT',
    'GET_CLIENT_PORT' : 'GET_CLIENT_PORT',
    'ANONYMITY' : 'ANONYMITY'


}

tokens += list(reserved.values())
t_ignore = ' \t'

def t_IP(t):
    r'\d+[.]\d+[.]\d+[.]\d+'
    return t
t_PERIOD = r'\.'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_error(t):
 print("Illegal character '%s'" % t.value[0])
 t.lexer.skip(1)

lexer = lex.lex()
