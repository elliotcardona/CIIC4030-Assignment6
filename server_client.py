import socket
import threading


port = 10000
socketFamily = socket.AF_INET
socketType = socket.SOCK_STREAM

def setPort(p):
    global port
    port = p

def setSocketFamily(sF):
    global socketFamily
    socketFamily = sF

def setSocketType(sT):
    global socketType
    socketType = sT


class Server:
    sock = socket.socket(socketFamily, socketType)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connections = []

    def __init__(self):
        self.sock.bind(('0.0.0.0',port))
        self.sock.listen(1)
        print("Server running...", self.sock.getsockname())
    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0])+':'+str(a[1])+ " connected")

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(bytes(data))
            if not data:
                print(str(a[0])+':'+str(a[1]), " disconnected")
                self.connections.remove(c)
                c.close()
                break

class Client:
    sock = socket.socket(socketFamily, socketFamily)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))

    def __init__(self, address):

        self.sock.connect((address, port))

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        print('Connected:')
        while True:
            data = self.sock.recv(1024)
            if(str(data, 'utf-8') == 'END_SESSION'):
                break
            if not data:
                break
            print(str(data, 'utf-8'))

def execute(t):
    print("Trying to connect...")
    if(t == 'client'):
        client = Client('127.0.0.1')
    else:
        server = Server()
        server.run()