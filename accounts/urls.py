from django.urls import path
from . import views
from knox import views as knox_views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('register/', views.RegisterView.as_view(), name='register'),
] 