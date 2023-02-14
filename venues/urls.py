from django.urls import path

from . import views


urlpatterns = [
    path('tenniscourts/', views.TennisCourtListAPIView.as_view(), name='tenniscourt-list'),
    path('tenniscourts/create/', views.TennisCourtCreateAPIView.as_view(), name='tenniscourt-create'),
    path('tenniscourts/<int:pk>/', views.TennisCourtRetrieveUpdateDestroyAPIView.as_view(), name='tenniscourt-detail'),
]