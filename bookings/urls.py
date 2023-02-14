from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookingListCreateAPIView.as_view(), name='booking-list'),
    path('<int:pk>/', views.BookingRetrieveUpdateDestroyAPIView.as_view(), name='booking-detail'),
]