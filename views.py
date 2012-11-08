from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from models import Post
from forms import PostForm


def index(request):
    query = Post.gql('ORDER BY date DESC')
    form = PostForm()
    return render_to_response('index.html',
                              {'posts': query.fetch(20), 'form': form})


def sign(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = Post(author=form.cleaned_data['author'],
                    message=form.cleaned_data['message'])
        post.put()

    return HttpResponseRedirect('/')
