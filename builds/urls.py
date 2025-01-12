from . import views
from django.urls import path

urlpatterns = [
    path("", views.BuildPostList.as_view(), name='home'),
    path('createbuildpost/', views.CreateBuildPost.as_view(), name='create_build_post'),
    path('<slug:slug>/', views.show_build_post, name='show_build_post'),
    path('delete/<slug:pk>/', views.DeleteBuildPost.as_view(), name='delete_build_post'),
    path('edit/<slug:pk>/', views.EditBuildPost.as_view(), name='edit_build_post'),
    path("<slug:slug>/edit_comment/<int:comment_id>/", views.edit_comment, name='edit_comment'),
    path("<slug:slug>/delete_comment/<int:comment_id>/", views.delete_comment, name='delete_comment'),
]