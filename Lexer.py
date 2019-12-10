import ply.lex as lex

tokens = [
    'IP',
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
    'GET_SS_FAMILY' : 'GET_SS_FAMILY',
    'ANONIMITY' : 'ANONIMITY'


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
    print ("ID: '%s'" % t.value)
    return t


def t_error(t):
 print("Illegal character '%s'" % t.value[0])
 t.lexer.skip(1)

lexer = lex.lex()

#testing lexer
#data1 = r'ssd'
#data2 = r'START_SERVER'
#data3 = r'END_SERVER'

#print ("Data: '%s'" % data0)
#print ("Data: '%s'" % data1)
#print ("Data: '%s'" % data2)
#print ("Data: '%s'" % data3)


#lexer.input(data0)
#lexer.input(data1)
#lexer.input(data2)
#lexer.input(data3)

#while True:
#   tok = lexer.token()
#   if not tok: break
#s   print (tok)
