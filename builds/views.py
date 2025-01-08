from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BuildPost, Comment
from .forms import CreateBuildsPost

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

def show_build_post(request, slug):
    """
    Displays/Shows singular build post with all it's content
    """
    queryset = BuildPost.objects.filter(status_build_post=2)
    build = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "builds/show_build_post.html",
        {"build": build},
    )


class CreateBuildPost(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    A logged in user can add a build post to the database through this class
    1. create form in forms.py
    2. add success message & link url
    3. validate build post method
    4. show success message method
    """
    form_class = CreateBuildsPost
    template_name = 'create_build_post.html'
    success_message = "Build post was created successfully"
    def form_valid(self, form):
        """
        When valid form has been added to form fields,
        logged in user will become the author automatically
        """
        form.instance.build_author = self.request.user
        return super().form_valid(form)

    #look more into it before I use it --> way we did it in class might be better tbh
    # Source: https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
    # here other source: https://stackoverflow.com/questions/4802482/how-to-send-success-message-if-we-use-django-generic-views (put in method description.....)
    def get_success_message(self, cleaned_data):
        """
        Overwrite default succes message method
        """
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )