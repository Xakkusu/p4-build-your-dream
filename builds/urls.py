from . import views
from django.urls import path

urlpatterns = [
    path("", views.BuildPostList.as_view(), name='home'),
    path('createbuildpost/', views.CreateBuildPost.as_view(), name='create_build_post'),
    path('<slug:slug>/', views.show_build_post, name='show_build_post'),
]