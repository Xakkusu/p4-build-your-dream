from django.contrib import admin
from .models import BuildPost, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(BuildPost)
admin.site.register(Comment)