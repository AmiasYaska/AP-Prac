from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegistrationView


urlpatterns = [
    # User registration
    path('register/', RegistrationView.as_view(), name='register'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),

]
