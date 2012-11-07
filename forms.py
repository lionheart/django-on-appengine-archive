from models import Post
from google.appengine.ext.db import djangoforms


class GuestbookForm(djangoforms.ModelForm):
    class Meta:
        model = Post
