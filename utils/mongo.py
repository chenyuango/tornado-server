from motor.motor_tornado import MotorClient
from utils.decorator import singleton


@singleton
class AsyncMongoConn(object):
    def __init__(self, mongodb_url):
        self.conn = MotorClient(mongodb_url)

    @property
    def connection(self):
        return self.conn
