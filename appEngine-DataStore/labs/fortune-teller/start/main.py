#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import random
import jinja2


def get_fortune():
    #add a list of fortunes to the empty fortune_list array
    fortune_list=['the grass is greener where you water it',
                  'doubt kills more dreams than failure ever will',
                  'be a voice, not an echo',
                  'happy thoughts',
                  'c\'est la vie',
                  'see the good',
                  'create your own sunshine']
    #use the random library to return a random element from the array
    random_fortune = random.choice(fortune_list)

    return random_fortune


#remember, you can get this by searching for jinja2 google app engine
template_loader = jinja2.FileSystemLoader(searchpath="./")
jinja_current_directory = jinja2.Environment(loader=template_loader)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_fortune())
        results_template = jinja_current_directory.get_template('templates/fortune-results.html')
        self.response.write(results_template.render())
    #add a post method
    #def post(self):

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World. Welcome to the root route of my app')

class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('My response is Goodbye World.')


#the route mapping
app = webapp2.WSGIApplication([
    #this line routes the main url ('/')  - also know as
    #the root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/predict', FortuneHandler), #maps '/predict' to the FortuneHandler
    ('/goodbye', GoodbyeHandler)
], debug=True)
