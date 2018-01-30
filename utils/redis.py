import aioredis
import asyncio

from utils.decorator import singleton
from config import REDIS_URL


@singleton
class AsyncRedisConn(object):

    @asyncio.coroutine
    def init(self):
        self.conn = yield from aioredis.create_redis(REDIS_URL)

    @property
    def connection(self):
        return self.conn

    @asyncio.coroutine
    def close(self):
        self.conn.close()
        yield from self.conn.wait_closed()
