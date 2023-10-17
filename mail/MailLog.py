import sys
sys.path.append('../config')
from config.Config import Config
from . Mail import Mail

class MailLog:

    @staticmethod
    def sendLog(filename):
        body = MailLog.__readLogFile(filename)
        Mail.sendMail(body)

    @staticmethod
    def __readLogFile(filename):
        try:
            f = open(filename, 'r')
            return """\n""" + f.read()
        except:
            return """\nLog file cannot be found! Please, review your configuration."""
