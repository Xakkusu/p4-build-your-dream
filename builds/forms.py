from django import forms
from .models import BuildPost

class CreateBuildsPost(forms.ModelForm):
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
        fields =["build_title", "image_of_build", "image_alt", 
                "build_description", "money_spent", "year_build"]