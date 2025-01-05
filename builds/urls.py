from . import views
from django.urls import path

urlpatterns = [
    path("", views.BuildPostList.as_view(), name='home'),
]