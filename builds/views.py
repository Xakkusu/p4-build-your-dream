from django.shortcuts import render, get_object_or_404
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
    template_name = "builds/index.html"
    paginate_by = 8

#def show_build_post(request, build_title):
#    """
#    Displays/Shows singular build post with all it's content
#    """
#    queryset = BuildPost.objects.filter(status_build_post=2)
#    build_post = get_object_or_404(queryset, build_title=build_title)
#
#   return render(
#        request,
#        "builds/show_build_post.html",
#        {"build_post": build_post},
#    )