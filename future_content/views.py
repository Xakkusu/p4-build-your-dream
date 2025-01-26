from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import FutureContentRequest
from .forms import FutureContentRequestForm
from django.contrib import messages
from django.core.paginator import Paginator


def create_future_content_request(request):
    """
    View for the user to give future request input
    and paginate the requests
    """

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
    future_content_request_count = future_content_request.filter(status_of_request = 2).count()

    paginate_by = 4

    paginator = Paginator(FutureContentRequest.objects.filter(status_of_request=2).order_by("created_on"), 4)

    page_number = request.GET.get('page')

    reqs = paginator.get_page(page_number)

    return render(
        request,
        "future_content/future_content.html",
        {"future_content_request": future_content_request,
         "reqs" : reqs,
         "paginate_by": paginate_by,
         "future_content_request_count":future_content_request_count,
         "future_content_request_form": future_content_request_form},
    )
