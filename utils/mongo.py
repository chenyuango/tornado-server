from motor.motor_tornado import MotorClient
from utils.decorator import singleton
from config import MONGODB_URL


@singleton
class AsyncMongoConn(object):

    def __init__(self):
        self.conn = MotorClient(MONGODB_URL)

    @property
    def connection(self):
        return self.conn
