from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager
from django.core.validators import MaxValueValidator, MinValueValidator

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
    money_spent = models.DecimalField(max_digits=8, decimal_places=2,
                                      validators=[MaxValueValidator(999999.99),
                                                  MinValueValidator(0.00)])
    year_build = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    status_build_post = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    liked = models.ManyToManyField(User, default=None, blank=True,
                                   related_name="liked")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.build_title} | written by {self.build_author}"

    @property
    def num_likes(self):
        """
        getting the number of likes
        """
        return self.liked.all().count()


LIKE_CHOICES = (("Like", "Like"), ("Unlike", "Unlike"))


class Comment(models.Model):
    """
    Model to store a single comment entry related to :model:`auth.User`
    and :model:`build_dream.BuildPost`. Needs to be approved
    """
    build_post = models.ForeignKey(BuildPost, on_delete=models.CASCADE,
                                   related_name="comments")
    comment_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment_body} by {self.comment_author}"
