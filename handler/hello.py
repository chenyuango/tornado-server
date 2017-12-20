from .base import BaseHandler


class HelloHandler(BaseHandler):
    def initialize(self):
        super(HelloHandler, self).initialize()

    def get(self):
        self.write('Hello World')
        self.finish()

    def post(self):
        self.write('Hello World')
        self.finish()