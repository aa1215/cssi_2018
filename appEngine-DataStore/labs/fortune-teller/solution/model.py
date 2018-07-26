from google.appengine.ext import ndb

class Movie(ndb.Model):
    title = ndb.StringProperty()
    # media_type = ndb.StringProperty(required=True, default="Movie")
    runtime = ndb.IntegerProperty(required=False)
    rating = ndb.FloatProperty(required=False)
    year = ndb.IntegerProperty(required=False)

    # def __init__(self, movie_title, run_time, user_rating):
    #     self.title = movie_title
    #     self.runtime_mins = run_time
    #     self.rating = user_rating

class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    billing = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)

    # def __init__(self, user, passw, bill, mail):
    #     self.username = user
    #     self.password = passw
    #     self.bill = bill
    #     self.email = mail

# class TVShow(ndb.model):
#     title = ndb.StringProperty(required=True)
#     genre = ndb.StringProperty(required=True)
