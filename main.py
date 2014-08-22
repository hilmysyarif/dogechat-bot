import random

import irc
from config import *

balance_requester = ""


def bind(self, msg):
    rawmsg = msg.split()
    filmsg = ' '.join(rawmsg[3:])[1:]
    source = rawmsg[2]
    sourcenick = rawmsg[0][1:].split("!")[0]
    if sourcenick == "Doger" and source == config['nick']:
        if "you tried" in filmsg.lower():
            ourbal = int(filmsg.split(" ")[10][2:])
            short = int(filmsg.split(" ")[5][2:]) - ourbal
            self.sendmsg(config['channels'][0], "Oops. Sorry, but I cannot proceed your win, because I'm D"
                         + str(short) + " short :(.")
        elif "your balance" in filmsg.lower():
            ourbal = int(filmsg.split(" ")[4][2:])
            global balance_requester
            self.sendmsg(balance_requester, "My balance is " + str(ourbal) + ".")
    if filmsg.lower() == "!help":
        self.sendmsg(source, "Hi! I am DogeChat, a IRC waterbowl bot made by SopaXorzTaker, please donate by \n"
                             "!tip dogechat-bot <amount> \n"
                             "My commands are: !dcbal - checks my balance")
    elif filmsg.split(" ")[0] == "!dcdo" and sourcenick in config['owners']:
        command = " ".join(filmsg.split(" ")[1:])
        try:
            out = eval(command)
            self.sendmsg(source, str(out))
        except:
            self.sendmsg(source, "Error executing command :P")
    elif filmsg.lower() == "!dcbal":
        balance_requester = source
        self.sendmsg("Doger", "balance")
        self.sendmsg(source, "Fetching balance...")

    elif source in config['channels'] and random.randint(0, 10) == 5 and not sourcenick in config['excluded_nicks'] \
            and len(filmsg) > 9:
        dogewon = random.randint(10, 50)
        self.sendmsg(source, "Wow! " + sourcenick + " just won " + str(dogewon) + " doges!")
        self.sendmsg("Doger", "tip " + sourcenick + " " + str(dogewon))


def init(self):
    self.sendmsg("NickServ", "identify " + config['pass'])


client = irc.IRCClient("irc.freenode.net", 6667, config['nick'], config['channels'], bind, init).client
