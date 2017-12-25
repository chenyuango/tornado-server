# -*- coding: utf-8 -*-
import asyncio

import tornado.httpserver
import tornado.ioloop
import tornado.netutil
import tornado.process
import tornado.web

from config import PROCESSES, PORT, MONGODB_URL
from utils.mongo import AsyncMongoConn
from handler.hello import HelloHandler
from handler.mongo import MongoHandler


application = tornado.web.Application([
    ('/hello', HelloHandler),
    ('/mongo', MongoHandler),
], )


def init_db():
    AsyncMongoConn(MONGODB_URL)


def main():
    sockets = tornado.netutil.bind_sockets(PORT)
    if PROCESSES != 1:
        tornado.process.fork_processes(PROCESSES)
    # configure tornado to use asyncio
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    server = tornado.httpserver.HTTPServer(application, xheaders=True)
    server.add_sockets(sockets)
    init_db()
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
