import Parser as parser

print('Welcome')
while True:
    try:
        s = input('S > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)