from django.views import generic
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def blog_index(request):

    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'index.html', context)


def post_detail(request, pk):
    return HttpResponse()


def make_post(request):

    return HttpResponse()
