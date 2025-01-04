from django.shortcuts import render
from django.views import generic
from .models import BuildPost, Comment

# Create your views here.
class BuildPostList(generic.ListView):
    """
    Returns all published  build-posts and displays 8 posts 
    per page paginated based on the date of creation.
    """
    #model = BuildPost
    queryset = BuildPost.objects.filter(status_build_post=2).order_by("created_on")
    #queryset = BuildPost.objects.filter(status=1).order_by("created_on")
    template_name = "index.html"
    #paginate_by = 8
    