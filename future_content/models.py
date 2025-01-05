from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Request Sent"), (1, "Request being looked at"), (2, "Will be implemented"), (3, "Denied"))

class FutureContentRequest(models.Model):
    """
    Model to store request from the user about possible future 
    content for the website
    """
    future_content_title = models.CharField(max_length=150, unique=True)
    future_content_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="future_content_request"
    )
    email_for_contact = models.EmailField(max_length=300)
    future_content_description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status_of_request = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.future_content_title} | requested by {self.future_content_author} | on {self.created_on}"