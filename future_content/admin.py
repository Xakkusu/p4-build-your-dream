from django.contrib import admin
from .models import FutureContentRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(FutureContentRequest)
class RequestAdmin(SummernoteModelAdmin):
    list_display = ('future_content_title', 'future_content_author',
                    'status_of_request')
    search_fields = ['future_content_title', 'status_of_request']
    list_filter = ('status_of_request', 'created_on')
    summernote_fields = ('future_content_description',)
