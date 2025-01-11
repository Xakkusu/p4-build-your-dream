from . import views
from django.urls import path

urlpatterns = [
    path('', views.create_future_content_request, name='future_content'),
]