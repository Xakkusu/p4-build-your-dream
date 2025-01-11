from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import FutureContentRequest
from .forms import FutureContentRequestForm

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

    

#def make_future_content_request(request):
#    """
#    User can make request to the Website owner about
#    future content that could be added
#    """

class CreateFutureContentRequest(generic.CreateView):
    """"
    A logged in  User can make request to the Website owner about
    future content that could be added
    Help from: https://www.youtube.com/watch?v=vXMTp_1_L7Y&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=10
    """
    template_name = "future_content/create_future_content_request.html"
    model = FutureContentRequest
    form_class = FutureContentRequestForm
    success_url = "/"

    def form_valid(self, form):
        """
        When valid form has been added to form fields,
        logged in user will become the author automatically
        """
        form.instance.future_content_author = self.request.user
        return super(CreateFutureContentRequest, self).form_valid(form)