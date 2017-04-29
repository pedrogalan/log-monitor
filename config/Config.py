from ConfigParser import ConfigParser
from os.path import expanduser

def getConfigFileName():
    return expanduser("~") + '/.log-monitor'

def loadProperties():
    config = ConfigParser()
    try:
        with open(getConfigFileName()) as f:
            config.readfp(f)
    except IOError:
        createDefaultProperties()
        config.read(getConfigFileName())
    return config

def createDefaultProperties():
    file = open(getConfigFileName(), "w")
    file.write("[all]\n\n")
    file.write("mail.smtp.host=change-me\n")
    file.write("mail.smtp.username=change-me\n")
    file.write("mail.smtp.password=change-me\n")
    file.write("mail.receiver=Mr. Change Me <change@me.com>\n")
    file.write("mail.sender=Mr. Change Me <change@me.com>\n\n")
    file.write("log.file.locations=/change/me.log,/also/change/this.log")
    file.close()

class Config:
    __properties = loadProperties()

    @staticmethod
    def get(name):
        try:
            return Config.__properties.get('all', name)
        except:
            logging.error("Configuration property %s not found in %s", name, getConfigFileName())
