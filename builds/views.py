from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import BuildPost, Comment
from .forms import CreateBuildsPostForm, CreateCommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from taggit.models import Tag
from .serializers import BuildPostSerializer
from rest_framework.generics import ListAPIView
from django.core.paginator import Paginator


# Create your views here.
def build_post_list(request):
    """
    Returns all published  build-posts and displays 8 posts
    per page paginated based on the date of creation.
    """
    tags = Tag.objects.all()

    paginator = Paginator(BuildPost.objects.
                          filter(status_build_post=2).
                          order_by("created_on"), 8)

    page_number = request.GET.get('page')

    builds = paginator.get_page(page_number)

    paginate_by = 8
    user = request.user
    context = {
              'builds': builds,
              'tags': tags,
              "paginate_by": paginate_by,
              'user': user
              }
    return render(request, 'builds/index.html', context)


def search_build_tags_list(request):
    """
    Returns all published  build-posts and displays 8 posts
    per page paginated based on the date of creation.
    Also shows tags, for tags/taggit I used this Tutorial:
    https://www.youtube.com/watch?v=213swbH8j_o
    """
    builds = BuildPost.objects.filter(
             status_build_post=2).order_by("created_on")
    tags = Tag.objects.all()
    paginate_by = 8
    context = {'builds': builds, 'tags': tags, "paginate_by": paginate_by}
    return render(request, 'builds/search_build_tags.html', context)


class BuildListAPIView (ListAPIView):
    """
    Returns a serlialized list used for the tags later on
    """
    queryset = BuildPost.objects.filter(status_build_post=2)
    serializer_class = BuildPostSerializer


def show_build_post(request, slug):
    """
    Displays/Shows singular build post with all it's content
    Comments can be created on this content
    """
    queryset = BuildPost.objects.filter(status_build_post=2)
    build = get_object_or_404(queryset, slug=slug)
    comments = build.comments.all().order_by("-created_on")
    comment_count = build.comments.filter(approved=True).count()

    if request.method == "POST":
        create_comment_form = CreateCommentForm(data=request.POST)
        if create_comment_form.is_valid():
            comment = create_comment_form.save(commit=False)
            comment.comment_author = request.user
            comment.build_post = build
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "We recceived your comment, it is waiting for approval!"
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


def edit_comment(request, slug, comment_id):
    """
    user can edit comment
    """
    if request.method == "POST":
        builds = BuildPost.objects.all()
        build = get_object_or_404(builds, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        create_comment_form = CreateCommentForm(data=request.POST,
                                                instance=comment)
        if create_comment_form.is_valid() and \
           comment.comment_author == request.user:
            comment = create_comment_form.save(commit=False)
            comment.build_post = build
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')
    return HttpResponseRedirect(reverse('show_build_post', args=[slug]))


def delete_comment(request, slug, comment_id):
    """
    user can delete their own comment
    """
    builds = BuildPost.objects.all()
    build = get_object_or_404(builds, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.comment_author == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Your comment has been deleted!'
        )
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')
    return HttpResponseRedirect(reverse('show_build_post', args=[slug]))


class CreateBuildPost(SuccessMessageMixin, generic.CreateView):
    """"
    A logged in user can add a build post to the database through this class
    Help from: https://www.youtube.com/watch?v=vXMTp_1_L7Y&list=
    PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=10
    """
    template_name = "builds/create_build_post.html"
    model = BuildPost
    form_class = CreateBuildsPostForm
    success_url = "/"
    success_message = "Your build is waiting for approval."

    def form_valid(self, form):
        """
        When valid form has been added to form fields,
        logged in user will become the author automatically
        """
        form.instance.build_author = self.request.user
        return super(CreateBuildPost, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        display success message
        Source: https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
        here other source:
        https://stackoverflow.com/questions/4802482/how-to-send-success-message
        -if-we-use-django-generic-views
        """
        return self.success_message % dict(
            cleaned_data,
            build_title=self.object.build_title,
        )


class EditBuildPost(LoginRequiredMixin,  UserPassesTestMixin,
                    SuccessMessageMixin, generic.UpdateView):
    """
    used tutorial from: https://www.youtube.com/watch?v=JzDBCZTgVyw&list=
    PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=14
    to edit a Post and redirect the user to a seperate html
    to make the edit
    Only the user that wrote the post can edit it.
    """
    model = BuildPost
    template_name = "builds/edit_build_post.html"
    form_class = CreateBuildsPostForm
    success_message = "Your build post has been successfully edited"

    def test_func(self):
        """
        is needed for the UserPassesTestMixin to work
        returns True or False
        True will let user edit build post
        """
        return self.request.user == self.get_object().build_author

    def get_success_url(self, **kwargs):
        """
        display success message when editing a post
        used: https://stackoverflow.com/questions/26897050/
        django-success-url-using-kwargs
        since the one for create builddpost did not work
        """
        if self.object.id is not None:
            return reverse('show_build_post', args=[self.object.slug])
        else:
            return reverse('home')


class DeleteBuildPost(SuccessMessageMixin, LoginRequiredMixin,
                      UserPassesTestMixin, generic.DeleteView):
    """
    used tutorial from:
    https://www.youtube.com/watch?v=nFa3lC105dM&list=PLXuTq6OsqZjbCS
    fiLNb2f1FOs8viArjWy&index=13
    to delete a Post and redirect the user to a seperate html
    to confirm the deletion
    Only the user that wrote the post can delete it
    """
    model = BuildPost
    template_name = "builds/delete_build_post.html"
    success_message = "Your build post has been successfully deleted"
    success_url = "/"

    def test_func(self):
        """
        is needed for the UserPassesTestMixin to work
        returns True or False
        True will delete
        """
        return self.request.user == self.get_object().build_author

    def delete(self, request, *args, **kwargs):
        """
        after succesfull deletion a sucess message i displayed
        Used to show success message:
        https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.SUCCESS(self.request, self.success_message)
        return super(DeleteBuildPost, self).delete(request, *args, **kwargs)


def like_buildpost(request, slug, *args, **kwargs):
    """
    Select and unselect the like-button
    got a tutorial and how to write the code instruction from:
    https://github.com/FlorianS4/project_4_django
    """
    if request.method == "POST":
        buildpost = get_object_or_404(BuildPost, slug=slug)
        if buildpost.liked.filter(id=request.user.id).exists():
            buildpost.liked.remove(request.user)
        else:
            buildpost.liked.add(request.user)
    return HttpResponseRedirect(reverse('show_build_post', args=[slug]))
