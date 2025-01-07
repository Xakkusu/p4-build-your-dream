from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "In Progress"), (2, "Approved"))

class BuildPost(models.Model):
    """
    Model to store a single build post entry related to :model:`auth.User`.
    """
    build_title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, default="", null=False)
    build_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="build_posts"
    )
    image_of_build = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(
       max_length=100, default="",
       null=False, blank=False
    )
    build_description = models.TextField()
    money_spent = models.DecimalField(max_digits=8, decimal_places=2)
    year_build = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    status_build_post = models.IntegerField(choices=STATUS, default=0)
    #should be automated from the description field
    excerpt = models.TextField(max_length=180, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.build_title} | written by {self.build_author}"


class Comment(models.Model):
    """
    Model to store a single comment entry related to :model:`auth.User`
    and :model:`build_dream.BuildPost`. Needs to be approved
    """
    build_id = models.ForeignKey(BuildPost, on_delete=models.CASCADE,
                             related_name="comments")
    comment_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    comment_title = models.CharField(max_length=100, unique=True)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    comment_status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.comment_body} by {self.comment_author}"