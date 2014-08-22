import socket
import threading


class IRCClient():
    address = ''
    port = 0
    nick = ""
    client = None
    sck = None
    bind = None

    def __main_thread__(self):
        print("DBG: started main thread")
        while self.running:
            data = self.sck.recv(1024).split("\n".encode('latin-1'))
            for line in data:
                if len(line) > 0:
                    print("< " + line.decode('latin-1'))
                    if "PING" in str(line):
                        # self.send(("PONG "+str(line).split(" ")[1]).encode('latin-1'))
                        self.send("PONG")
                    elif self.bind and "PRIVMSG ".encode('ascii') in line:
                        self.bind(self, line.decode('latin-1'))

    def __init__(self, address, port, nick, channels, bind=None, init=None):
        self.running = True
        self.address = address
        self.port = port
        self.nick = nick
        self.bind = bind
        self.init = init
        self.client = self
        self.sck = socket.socket()
        self.sck.connect((address, port))
        self._main_thread = threading.Thread(target=self.__main_thread__)
        self._main_thread.start()
        self.send("NICK " + self.nick)
        # self.send("MODE " + self.nick + " +x")
        self.send("USER %(nick)s %(nick)s %(nick)s :%(nick)s" % {'nick': self.nick})
        print("We are identified hooray!")
        for channel in channels:
            self.send("JOIN :" + channel)
            print("DBG: joined " + channel)
        self.init(self)

    def send(self, msg):
        print("> " + msg)
        self.sck.send((msg.replace("\n", "").replace("\r", "") + "\r\n").encode())

    def sendmsg(self, to, msg):
        for line in msg.split("\n"):
            self.send("PRIVMSG " + to + " :" + line)

    def me(self, to, action):
        self.send("PRIVMSG " + to + " :" + "\x01ACTION " + action + "\x01")

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.running = False