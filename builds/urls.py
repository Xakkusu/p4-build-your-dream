from . import views
from django.urls import path

urlpatterns = [
    path("", views.BuildPostList.as_view(), name='home'),
    #path('<build_title:build_title>/', views.show_build_post, name='show_build_post'),
]