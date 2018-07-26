import webapp2
import random
import json
import jinja2
from google.appengine.api import urlfetch
import urllib
import logging

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)

def get_meme_list():
    link = "https://api.imgflip.com/get_memes"
    result = urlfetch.fetch(link)
    #.loads function makes string into an object it can read
    json_result = json.loads(result.content)
    memes = json_result["data"]["memes"]
    listofmemes = []
    #creating a list that will contain all the urls of the memes
    #adding the meme urls from the "memes" dictionary to listofmemes
    for i in range(len(memes)):
        meme = memes[i]["id"]
        listofmemes.append(meme)
    return listofmemes

# def get_caption(mem, text1, text2):




class MainPage(webapp2.RequestHandler):
    def get(self):
        listofmemes = get_meme_list()
        randint = random.randint(1,len(listofmemes))
        self.response.headers['Content-Type'] = 'text/html'
        # for i in range(len(listofmemes)):
        sourc = listofmemes[randint]
        # self.response.write("<img src={s}>".format(s=sourc))

        random_text = [
            'This is a meme.',
            'This is a caption.',
            'This is a sentence.',
            'This is confusing.',
            'Text.',
            'Hehehe',
            'Hmmmm',
            'Cinnamon Toast Crunch',
            'Today is Tuesday',
            'It\'s 2018',
            'Ok so...?',
            'Herp Derp a Derp.']

        #captioning the memes
        caption_url = 'https://api.imgflip.com/caption_image'
        caption_dict = {
            'template_id': sourc,
            'username': 'aksharasanand',
            'password': 'puppy100',
            'text0': random.choice(random_text),
            'text1': random.choice(random_text),
            }
        try:
            logging.info('Trying to caption my meme...')
            result1 = urlfetch.fetch(
                url=caption_url,
                payload=urllib.urlencode(caption_dict),
                method=urlfetch.POST)
            # self.response.write(result.content)

            logging.info('Received the following response: {resp}'.format(
                resp=result1.content))
            new_meme_dict = json.loads(result1.content)
            picture_url = new_meme_dict['data']['url']
            self.response.write('<img src="{pic}"/>'.format(
                pic=picture_url))

        except Exception as e:
            # I don't know what exceptions might happen
            # so let's just catch all of them for now.
            self.response.write(
                'OH NOES Something went really wrong while '
                'captioning the meme: {e}'.format(e=e))

        # def create_captioned_meme()

class MemeTemp(webapp2.RequestHandler):
    def get(self):
        listofmemes = get_meme_list()
        template = template_env.get_template('templates/home.html')
        self.response.write(template.render({'memes': listofmemes}))

    def post(self):
        meme_type = self.request.get('meme-type')
        first_line = self.request.get('user-first-ln')
        second_line = self.request.get('user-second-ln')
        self.response.write("Line 2 that you inputted is {t} <br>".format(t=second_line))
        # meme_dict = create_captioned_meme(meme_type, top_text, bottom_text)

class RecipeBrowser(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/recipes.html')
        recipe = {'ingredients': ['carrots', 'chocolate'],
                  'cuisine': 'american'}
        self.response.write(template.render(recipe))

app = webapp2.WSGIApplication([
    ('/main', MainPage),
    ('/meme_temp', MemeTemp),
    ('/recipes', RecipeBrowser)
], debug=True)
