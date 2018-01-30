# -*- coding: utf-8 -*-
import asyncio

import tornado.httpserver
import tornado.ioloop
import tornado.netutil
import tornado.process
import tornado.web

from config import PROCESSES, PORT
from utils.mongo import AsyncMongoConn
from utils.redis import AsyncRedisConn

from handler.hello import HelloHandler
from handler.mongo import MongoHandler
from handler.redis import RedisHandler


application = tornado.web.Application([
    ('/hello', HelloHandler),
    ('/mongo', MongoHandler),
    ('/redis', RedisHandler),
], )


@asyncio.coroutine
def init():
    AsyncMongoConn()
    yield from AsyncRedisConn().init()


@asyncio.coroutine
def destroy():
    yield from AsyncRedisConn().close()


def main():
    sockets = tornado.netutil.bind_sockets(PORT)
    if PROCESSES != 1:
        tornado.process.fork_processes(PROCESSES)
    # configure tornado to use asyncio
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    server = tornado.httpserver.HTTPServer(application, xheaders=True)
    server.add_sockets(sockets)
    try:
        asyncio.get_event_loop().run_until_complete(init())
        asyncio.get_event_loop().run_forever()
    finally:
        asyncio.get_event_loop().run_until_complete(destroy())

if __name__ == "__main__":
    main()
