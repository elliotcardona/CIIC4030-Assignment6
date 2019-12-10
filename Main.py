import Parser as parser

print('Welcome')
while True:
    try:
        s = input('S > ')
    except EOFError:
        break
    except KeyboardInterrupt:
        break
    if not s: continue
    result = parser.parser.parse(s)
    print(result)