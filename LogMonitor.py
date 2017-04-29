import sys
from config.Config import Config
from mail.MailLog import MailLog

class LogMonitor:

    @staticmethod
    def check():
        logFileLocations = Config.get('log.file.locations').split(',')
        for logFileLocation in logFileLocations:
            LogMonitor.__checkLogFile(logFileLocation)

    @staticmethod
    def __checkLogFile(filename):
        if LogMonitor.__areThereErrors(filename):
            MailLog.sendLog(filename)
            LogMonitor.__clearFile(filename)

    @staticmethod
    def __areThereErrors(filename):
        if '[ERROR]' in open(filename).read():
            return True
        return False

    @staticmethod
    def __clearFile(filename):
        with open(filename, 'w'):
            pass
