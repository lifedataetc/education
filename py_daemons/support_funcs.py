import logging
import time
from logging.handlers import SysLogHandler
from service import find_syslog, Service
from config import *

class Daemon_Class(Service):
    def __init__(self, *args, **kwargs):
        super(daemon_class, self).__init__(*args, **kwargs)
        self.logger.addHandler(SysLogHandler(address=find_syslog(), facility=SysLogHandler.LOG_DAEMON))
        self.logger.setLevel(logging.INFO)
        # settings and setup

    # run the process
    def run(self,*args, **kwargs):
        while not self.got_sigterm():
            # process code here

# end python-service