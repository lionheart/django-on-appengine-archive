import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from google.appengine.api import users
from google.appengine.ext import ndb

from models import Post
from forms import GuestbookForm


def index(request):
    query = Post.gql('ORDER BY date DESC')
    form = GuestbookForm()
    return render_to_response('index.html',
                            {'posts': query.fetch(20),
                             'form': form
                            }
                           )


def sign(request):
    form = GuestbookForm(request.POST)
    if form.is_valid():
        form.save()

    return HttpResponseRedirect('/')
