import ply.lex as lex

tokens = [
    'IP',
    'NUMBER',
    'PERIOD',
    'ID'
]

reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while': 'WHILE',
    'for' : 'FOR',
    'START_SERVER' : 'START_SERVER',
    'END_SERVER' : 'END_SERVER',
    'CREATE_CLIENT' : 'CREATE_CLIENT',
    'END_CLIENT' : 'END_CLIENT'

}

tokens += list(reserved.values())
t_PERIOD = r'\.'
t_ignore  = ' \t'

def t_IP(t):
    r'\d+[.]\d+[.]\d+[.]\d+'
    return t

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
data0 = r'123.423.423.1'
data1 = r'ssd'
data2 = r'START_SERVER'
data3 = r'END_SERVER'

print ("Data: '%s'" % data0)
print ("Data: '%s'" % data1)
print ("Data: '%s'" % data2)
print ("Data: '%s'" % data3)


lexer.input(data0)
lexer.input(data1)
#lexer.input(data2)
#lexer.input(data3)

while True:
   tok = lexer.token()
   if not tok: break
   print (tok)
