from django.http import HttpResponse
from django.views import generic
from blog.models import Post  


class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World!')


class PostListView(generic.ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
