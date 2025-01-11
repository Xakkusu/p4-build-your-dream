from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import FutureContentRequest
from .forms import FutureContentRequestForm
from django.contrib import messages

# Create your views here.


def create_future_content_request(request):
    """
    """
    paginate_by = 4

    if request.method == "POST":
        future_content_request_form = FutureContentRequestForm(data=request.POST)
        if future_content_request_form.is_valid():
            content_request = future_content_request_form.save(commit=False)
            content_request.future_content_author = request.user
            content_request.save()
            messages.add_message(
                request, messages.SUCCESS,
                "We recceived your request, after it is approved and it is deemed to be suitable for us, it will be shown here!"
            )
    future_content_request = FutureContentRequest.objects.filter(status_of_request=2).order_by("created_on")
    future_content_request_form = FutureContentRequestForm()

    return render(
        request,
        "future_content/future_content.html",
        {"future_content_request": future_content_request,
         "paginate_by": paginate_by,
         "future_content_request_form": future_content_request_form},
    )


#class FutureRequestList(generic.ListView):
#    """
#    Returns all requests that will be implemented displays 4 requests 
#    per page paginated based on the date of creation.
#    """
#    #model = BuildPost
#    queryset = FutureContentRequest.objects.filter(status_of_request=2).order_by("created_on")
#    template_name = "future_content/future_content.html"
#    paginate_by = 4
#    def create_future_content_request(request):
#        future_content_request_form = FutureContentRequestForm()
#        future_content_request_count = build.queryset.filter(status_of_request = 2).count()
#        
#        if request.method == "POST":
#            future_content_request_form = FutureContentRequestForm(data=request.POST)
#            if future_content_request_form.is_valid():
#                future_content_request = future_content_request_form.save(commit=False)
#                future_content_request.future_content_author = request.user
#                future_content_request.save()
#                messages.add_message(
#                    request, messages.SUCCESS,
#                    "We recceived your request, after it is approved and it is deemed to be suitable for us, it will be shown here!"
#                )
#        future_content_request_form = FutureContentRequestForm()
#
#        return render(
#            request,
#            "future_content/future_content.html",
#            {
#                "queryset": queryset,
#                "future_content_request_count": future_content_request_count,
#                "future_content_request_form": future_content_request_form
#            },
#        )

    

#def make_future_content_request(request):
#    """
#    User can make request to the Website owner about
#    future content that could be added
#    """

#def create_future_content_request(request):
#    """"
#    A logged in  User can make request to the Website owner about
#    future content that could be added
#    Help from: https://www.youtube.com/watch?v=vXMTp_1_L7Y&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=10
#    """
#    template_name = "future_content/future_content.html"
#    model = FutureContentRequest
#    form_class = FutureContentRequestForm
#    success_url = "/"
#
#    def form_valid(self, form):
#        """
#        When valid form has been added to form fields,
#        logged in user will become the author automatically
#        """
#        form.instance.future_content_author = self.request.user
#        return super(CreateFutureContentRequest, self).form_valid(form)