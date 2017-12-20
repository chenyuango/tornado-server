import tornado


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self._set_header()

    def _set_header(self):
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.set_header('Cache-Control', 'no-cache')
        self.set_header("Expires", "0")
