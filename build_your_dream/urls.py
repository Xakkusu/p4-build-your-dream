from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path("future-content/", include("future_content.urls"),
         name="future-content-urls"),
    path('summernote/', include('django_summernote.urls')),
    path("", include("builds.urls"), name="builds-urls"),
]
