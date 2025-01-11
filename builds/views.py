from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import BuildPost, Comment
from .forms import CreateBuildsPostForm, CreateCommentForm

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
    comments = build.comments.all().order_by("-created_on")
    comment_count = build.comments.filter(comment_status = 2).count()
    
    if request.method == "POST":
        create_comment_form = CreateCommentForm(data=request.POST)
        if create_comment_form.is_valid():
            comment = create_comment_form.save(commit=False)
            comment.comment_author = request.user
            comment.build_post = build
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "We recceived your comment, after it is approved it will be added to the post!"
            )
    create_comment_form = CreateCommentForm()

    return render(
        request,
        "builds/show_build_post.html",
        {
            "build": build,
            "comments": comments,
            "comment_count": comment_count,
            "create_comment_form": create_comment_form
        },
    )


#class CreateBuildPost(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
#    """
#    das hier mal probieren:
#
#    https://www.youtube.com/watch?v=wzZiONbtwiA
#
#    A logged in user can add a build post to the database through this class
#    1. create form in forms.py
#    2. add success message & link url
#    3. validate build post method
#    4. show success message method
#    """
#    form_class = CreateBuildsPost
#    template_name = 'create_build_post.html'
#    success_message = "Build post was created successfully"
#
#    def form_valid(self, form):
#        """
#        When valid form has been added to form fields,
#        logged in user will become the author automatically
#        """
#        form.instance.build_author = self.request.user
#        return super(CreateBuildPost, self).form_valid(form)
#
#    #look more into it before I use it --> way we did it in class might be better tbh
#    # Source: https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
#    # here other source: https://stackoverflow.com/questions/4802482/how-to-send-success-message-if-we-use-django-generic-views (put in method description.....)
#    def get_success_message(self, cleaned_data):
#        """
#        Overwrite default succes message method
#        """
#        return self.success_message % dict(
#            cleaned_data,
#            title=self.object.title,
#        )

class CreateBuildPost(generic.CreateView):
    """"
    A logged in user can add a build post to the database through this class
    Help from: https://www.youtube.com/watch?v=vXMTp_1_L7Y&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=10
    """
    template_name = "builds/create_build_post.html"
    model = BuildPost
    form_class = CreateBuildsPostForm
    success_url = "/"

    def form_valid(self, form):
        """
        When valid form has been added to form fields,
        logged in user will become the author automatically
        """
        form.instance.build_author = self.request.user
        return super(CreateBuildPost, self).form_valid(form)

class DeleteBuildPost(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    used tutorial from: https://www.youtube.com/watch?v=nFa3lC105dM&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=13
    to delete a Post and redirect the user to a seperate html
    to confirm the deletion
    Only the user that wrote the post can delete it
    """
    model = BuildPost
    success_url = "/"

    def test_func(self):
        """
        is needed for the UserPassesTestMixin to work
        returns True or False
        True will delete
        """
        return self.request.user == self.get_object().user