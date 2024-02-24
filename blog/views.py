from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from .models import Post


def home(request):
    blg_details = Blog.objects.all().values()
    post = Post.objects.all()
    template = loader.get_template('blog/index.html')
    context = {'details': blg_details}
    context_2 = {'Posts': post}
    return HttpResponse(template.render(context_2, request))

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html' # <app>/<model>_<viewtype.html>
    context_object_name = 'Posts' # what we will loop through . Same variable  as one 
                                                        # provided in the renderfunction. This is our list.

    ordering = ['-date_posted'] # ordering from newest to oldest.


class PostDetailView(DetailView):
    """
    This handles single's post detail and displays it in a single page

    so post_detail.html page is rendered since i have not declared destination
    as that of postlistview
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    provides a form for creating a post or editing a post
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        this overrides the form created and sets the user to the current user logged in to avoid the 
        integrity error.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    tmp = loader.get_template('blog/about.html')
    return HttpResponse(tmp.render())

def details(request, id):
    blg_details = Blog.objects.get(id=id)
    temp = loader.get_template('blog/details.html')
    context = {'blg_details': blg_details}
    return HttpResponse(temp.render(context, request))

