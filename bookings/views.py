from django.shortcuts import render
from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer
from api.mixins import BookingOwnerPermissionMixin
# Create your views here.


class BookingListCreateAPIView(
    BookingOwnerPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)



class BookingRetrieveUpdateDestroyAPIView(
    BookingOwnerPermissionMixin,
    generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

