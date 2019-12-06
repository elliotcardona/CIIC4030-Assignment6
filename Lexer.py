import ply.lex as lex

tokens = [
    'IP',
    'NUMBER',
    'STRING',
    'PERIOD'
]

reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while': 'WHILE',
    'for' : 'FOR',

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

def t_STRING(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    print ("String: '%s'" % t.value)

def t_error(t):
 print("Illegal character '%s'" % t.value[0])
 t.lexer.skip(1)

lexer = lex.lex()

#testing lexer
data = r'123.423.423.1'

print ("Data: '%s'" % data)

lexer.input(data)

while True:
   tok = lexer.token()
   if not tok: break
   print (tok)
