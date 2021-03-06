import socket
import sys
import threading


sPort = 10000
cPort = 10000
serverSocketFamily = socket.AF_INET
serverSocketType = socket.SOCK_STREAM
clientSocketFamily = socket.AF_INET
clientSocketType = socket.SOCK_STREAM
anonymity = False
running = False

def setAnonymity(state):
    global anonymity
    anonymity = state

def getAnonymity():
    global anonymity
    return anonymity

def setServerPort(p):
    if p < 1024:
        print("Port must have value higher than 1023")
        sys.exit(0)
    elif not running:
        global sPort
        sPort = p
    else:
        print("Server running, cannot change Port!")
        sys.exit(0)

def setClientPort(p):
    global cPort
    cPort = p

def setServerSocketFamily(sF):
    if not running:
        global serverSocketFamily
        serverSocketFamily = sF
    else:
        print("Server running, cannot change Socket Family!")
        sys.exit(0)

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
    connections = []

    def __init__(self):
        global running
        running = True
        self.sock = socket.socket(serverSocketFamily, serverSocketType)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
        T = False
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                if str(data, 'utf-8') == "END_SESSION" and connection == c:
                    T = True
                    break
                if not connection == c and str(data, 'utf-8') == "END_SESSION":
                    msg = "(" + str(a[0]) + ":" + str(a[1]) + ")" + "=> " + "LEFT_CHAT"
                    if not anonymity:
                        connection.send(bytes(msg, 'utf-8'))
                    else:
                        connection.send(bytes("LEFT_CHAT", 'utf-8'))
                elif not connection == c:
                    msg = "(" + str(a[0]) + ":" + str(a[1]) + ")" + "=> " + str(data,'utf-8')
                    if not anonymity:
                        connection.send(bytes(msg, 'utf-8'))
                    else:
                        connection.send(bytes(data))
            if not data or T:
                print(str(a[0])+':'+str(a[1]), " disconnected")
                self.connections.remove(c)
                c.close()
                break
    def sendExit(self):
        for connection in self.connections:
            connection.send(b'\x11')
class Client:
    eCode = ""
    sock = socket.socket(clientSocketFamily, clientSocketType)
    def sendMsg(self):
        while True:
            try:
                t = input("")
                self.sock.send(bytes(t, 'utf-8'))
            except OSError:
                pass
            if t == 'END_SESSION' or self.eCode == 'END_SESSION':
                self.sock.close()
                break


    def __init__(self, address):
        self.eCode = ""
        self.sock = socket.socket(clientSocketFamily, clientSocketType)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((address, cPort))

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        print('Connected:')
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            if data == b'\x11':
                self.eCode = 'END_SESSION'
                self.sock.close()
                break
            else:
                print(str(data, 'utf-8'))

def execute(t):
    print("Trying to connect...")
    if(t == 'client'):
        try:
            client = Client('0.0.0.0')
            #127.0.0.1
        except KeyboardInterrupt:
            pass
        except:
            print("Could not establish connection with server! Make sure server is running.")
    else:
        try:
            server = Server()
            server.run()
        except KeyboardInterrupt:
            server.sendExit()
            pass
        except:
            print("Could not start up the server!")