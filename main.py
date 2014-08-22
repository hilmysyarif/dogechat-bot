import irc, random
from config import *

def bind(self, msg):
    rawmsg = msg.split()
    filmsg = ' '.join(rawmsg[3:])[1:]
    source = rawmsg[2]
    sourcenick = rawmsg[0][1:].split("!")[0]

    if filmsg == "!help":
        self.sendmsg(source, "Hi! I am DogeChat, a IRC waterbowl bot, please donate by"
                             " /msg Doger tip dogechat-bot <amount>")
    elif source == channel and random.randint(0, 10) == 5 and not sourcenick in excluded_nicks and len(filmsg) > 9:
            dogewon = random.randint(1, 20)
            self.sendmsg(source, "Wow! " + sourcenick + " just won " + str(dogewon) + " doges!")
            self.sendmsg("Doger", "tip " + sourcenick + " " + str(dogewon))
            tipAttempted = True
def init(self):
    self.sendmsg("NickServ", config['pass'])
client = irc.IRCClient("irc.freenode.net", 6667, config['nick'], config['channels'], bind, init).client
excluded = open("excluded.txt", "r")
excluded_nicks = excluded.readlines()
excluded.close()