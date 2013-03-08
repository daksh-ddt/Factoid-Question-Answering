# -*- coding: utf-8 *-*
'''
{
"question": ["who was the first president"]
}

'''
import os
import json
import tornado.web
import tornado.ioloop
from tornado.options import define, options
import factoid_handler


class APIHandler(tornado.web.RequestHandler):

    def get(self):
        # Retrieve the question
        question = [self.get_argument("question", strip=True)]
        print 'Question:', question
        response = factoid.answer(question)
        self.write(response)


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('ask_get.html')

    def post(self):
        # Retrieve the question
        data_json = tornado.escape.json_decode(self.request.body)
        question = [data_json['question']]
        print 'Question:', question
        response = factoid.answer(question)
        self.write(response)


handlers = [
            (r"/", MainHandler),
            (r"/f", APIHandler)
            ]


settings = dict(template_path=os.path.join(
    os.path.dirname(__file__), "templates"))
application = tornado.web.Application(handlers, **settings)
define("port", default=8003, help="run on the given port", type=int)


if __name__ == "__main__":
    factoid = factoid_handler.Factoid_handler()
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
