from google.appengine.ext import db


class Post(db.Model):
    author = db.UserProperty()
    message = db.StringProperty(required=True)
    date = db.DateTimeProperty(auto_now_add=True)
