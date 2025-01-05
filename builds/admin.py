from django.contrib import admin
from .models import BuildPost, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BuildPost)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('build_title', 'money_spent', 'build_author', 'status_build_post')
    search_fields = ['build_title', 'build_description']
    list_filter = ('status_build_post', 'created_on')
    prepopulated_fields = {'slug': ('build_title',), 'excerpt': ('build_description',)}
    summernote_fields = ('build_description', 'excerpt')


# Register your models here.
admin.site.register(Comment)