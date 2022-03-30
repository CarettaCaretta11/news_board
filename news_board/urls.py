from django.contrib import admin
from django.urls import path, include
from base import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('api/', include('base.urls')),
]