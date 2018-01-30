import json
import asyncio
from .base import BaseHandler
from utils.redis import AsyncRedisConn


class RedisHandler(BaseHandler):
    def initialize(self):
        super(RedisHandler, self).initialize()
        self.redis_conn = AsyncRedisConn().connection

    @asyncio.coroutine
    def get(self):
        key = self.get_argument('key')
        if key:
            value = yield from self.redis_conn.get(key)
        else:
            value = ''
        self.write(value)
        self.finish()

    @asyncio.coroutine
    def post(self):
        data = self.request.body.decode()
        records = json.loads(data)
        for record in records:
            if not record or len(record) < 2:
                continue
            key, value = record[0], record[1]
            yield from self.redis_conn.set(key, value)
        self.write({'status': 'success'})
        self.finish()