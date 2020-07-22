from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('music.urls')),
    path('', include('history.urls')),
    path('admin/', admin.site.urls),
]
