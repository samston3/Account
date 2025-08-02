from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('templates/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('templates/register/', views.register_view, name='register'),
]
