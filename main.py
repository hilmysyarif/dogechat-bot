import irc, random
from config import *

def bind(self, msg):
    rawmsg = msg.split()
    filmsg = ' '.join(rawmsg[3:])[1:]
    source = rawmsg[2]
    sourcenick = rawmsg[0][1:].split("!")[0]

    if filmsg == "!help":
        self.sendmsg(source, "Hi! I am DogeChat, a IRC waterbowl bot made by SopaXorzTaker, please donate by \n"
                             "!tip dogechat-bot <amount> \n")
    elif source in config['channels'] and random.randint(0, 10) == 5 and not sourcenick in config['excluded_nicks'] \
            and len(filmsg) > 9:
            dogewon = random.randint(1, 20)
            self.sendmsg(source, "Wow! " + sourcenick + " just won " + str(dogewon) + " doges!")
            self.sendmsg("Doger", "tip " + sourcenick + " " + str(dogewon))

def init(self):
    self.sendmsg("NickServ", "identify " + config['pass'])
client = irc.IRCClient("irc.freenode.net", 6667, config['nick'], config['channels'], bind, init).client
