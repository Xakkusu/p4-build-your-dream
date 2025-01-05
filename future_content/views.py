from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import FutureContentRequest

# Create your views here.


class FutureRequestList(generic.ListView):
    """
    Returns all requests that will be implemented displays 4 requests 
    per page paginated based on the date of creation.
    """
    #model = BuildPost
    queryset = FutureContentRequest.objects.filter(status_of_request=2).order_by("created_on")
    template_name = "future_content/future_content.html"
    paginate_by = 4

    

def make_future_content_request(request):
    """
    User can make request to the Website owner about
    future content that could be added
    """