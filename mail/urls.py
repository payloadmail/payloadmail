from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='mail-login'),
    path('home/', views.home, name='mail-home'),
]
