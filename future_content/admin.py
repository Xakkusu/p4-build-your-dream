from django.contrib import admin
from .models import FutureContentRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(FutureContentRequest)
class RequestAdmin(SummernoteModelAdmin):
    list_display = ('future_content_title', 'future_content_author', 'status_of_request')
    search_fields = ['future_content_title', 'status_of_request']
    list_filter = ('status_of_request', 'created_on')
    summernote_fields = ('future_content_description',)

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.
