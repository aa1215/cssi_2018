import webapp2
import os
import jinja2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome to Akshara's Online Portal")

app = webapp2.WSGIApplication( [
    ('/hello', MainHandler),
], debug=True)
