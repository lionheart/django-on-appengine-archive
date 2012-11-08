from google.appengine.ext import ndb


class Post(ndb.Model):
    author = ndb.StringProperty()
    message = ndb.StringProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
