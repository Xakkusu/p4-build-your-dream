from . import views
from django.urls import path

urlpatterns = [
    path('', views.FutureRequestList.as_view(), name='future_content'),
]