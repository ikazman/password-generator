from django.contrib import admin
from django.urls import path

from generator import views

urlpatterns = [
    path('', views.index, name='index'),
    path('password/', views.generate_password, name='password'),
    path('admin/', admin.site.urls),
]
