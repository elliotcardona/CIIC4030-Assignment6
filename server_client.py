import socket
import threading


sPort = 10000
cPort = 10000
serverSocketFamily = socket.AF_INET
serverSocketType = socket.SOCK_STREAM
clientSocketFamily = socket.AF_INET
clientSocketType = socket.SOCK_STREAM


def setServerPort(p):
    global sPort
    sPort = p

def setClientPort(p):
    global cPort
    cPort = p

def setServerSocketFamily(sF):
    global serverSocketFamily
    serverSocketFamily = socket.sF

def setServerSocketType(sT):
    global serverSocketType
    serverSocketType = sT

def setClientSocketFamily(sF):
    global clientSocketFamily
    clientSocketFamily = sF

def setClientSocketType(sT):
    global clientSocketType
    clientSocketType = sT

def getServerPort():
    global sPort
    return sPort

def getClientPort():
    global cPort
    return cPort

def getServerSocketFamily():
    global serverSocketFamily
    return serverSocketFamily

def getServerSocketType():
    global serverSocketType
    return serverSocketType

def getClientSocketFamily():
    global clientSocketFamily
    return clientSocketFamily

def getClientSocketType():
    global clientSocketType
    return clientSocketType

class Server:
    sock = socket.socket(serverSocketFamily, serverSocketType)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connections = []

    def __init__(self):
        self.sock.bind(('0.0.0.0',sPort))
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
    sock = socket.socket(clientSocketFamily, clientSocketType)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))

    def __init__(self, address):

        self.sock.connect((address, cPort))

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        print('Connected:')
        while True:
            data = self.sock.recv(1024)
            #if(str(data, 'utf-8') == 'END_SESSION'):

            if not data:
                break
            print(str(data, 'utf-8'))

def execute(t):
    print("Trying to connect...")
    if(t == 'client'):
        try:
            client = Client('127.0.0.1')
        except KeyboardInterrupt:
            pass
        except:
            print("Could not establish connection with server! Make sure server is running.")
    else:
        try:
            server = Server()
            server.run()
        except KeyboardInterrupt:
            pass
        except:
            print("Could not start up the server!")
