from django import forms
from .models import FutureContentRequest

class FutureContentRequestForm(forms.ModelForm):
    """
    Class to create the form fields needed to create
    a request for future content by the user from the views
    """
    class Meta:
        """
        Specify the model used and which fields will be
        in the form
        """
        model = FutureContentRequest
        fields =["future_content_title", "email_for_contact", 
                "future_content_description"]