from django import forms
from .models import BuildPost, Comment

class CreateBuildsPostForm(forms.ModelForm):
    """
    Class to create the form fields needed to create
    a build post by the user from the views
    """
    class Meta:
        """
        Specify the model used and which fields will be
        in the form
        """
        model = BuildPost
        fields =["build_title", "image_of_build",  
                "build_description", "money_spent", "year_build"]

class CreateCommentForm(forms.ModelForm):
    """
    Class to create the form fields needed to create
    a comment by the user from the views
    """
    class Meta:
        """
        Specify the model used and which fields will be
        in the form
        """
        model = Comment
        fields =["comment_body"]