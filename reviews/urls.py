from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReviewListAPIView.as_view()),
    path('create/', views.ReviewCreateAPIView.as_view()),
    path('<int:pk>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view()),
    path('<int:pk>/responses/', views.ResponseListCreateAPIView.as_view()),
    path('<int:pk>/responses/<int:response_pk>/', views.ResponseRetrieveUpdateDestroyAPIView.as_view()),
]