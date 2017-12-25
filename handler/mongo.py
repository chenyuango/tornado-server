import json
import asyncio
from .base import BaseHandler
from utils.mongo import AsyncMongoConn


class MongoHandler(BaseHandler):
    def initialize(self):
        super(MongoHandler, self).initialize()
        self.mongo_conn = AsyncMongoConn().connection

    @asyncio.coroutine
    def get(self):
        db = self.mongo_conn.test
        result = []
        cursor = db.test.find({}, {'_id': 0}).limit(10)
        for doc in (yield cursor.to_list(None)):
            result.append(doc)
        self.write(json.dumps(result))
        self.finish()

    @asyncio.coroutine
    def post(self):
        data = self.request.body.decode()
        records = json.loads(data)
        db = self.mongo_conn.test
        for record in records:
            db.test.save(record)
        self.write({'status': 'success'})
        self.finish()