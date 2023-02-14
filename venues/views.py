from rest_framework import generics
from .serializers import TennisCourtSerializer, TennisCourtListSerializer
from .models import TennisCourt
from api.mixins import VenueOwnerPermissionMixin
from rest_framework.parsers import MultiPartParser, FormParser



class TennisCourtListAPIView(
    VenueOwnerPermissionMixin,
    generics.ListAPIView):
    queryset = TennisCourt.objects.all()
    serializer_class = TennisCourtListSerializer
    pareser_classes = (MultiPartParser, FormParser)


    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_venue_owner:
            return self.queryset.filter(user=self.request.user)
        return self.queryset.all()


class TennisCourtCreateAPIView(
    VenueOwnerPermissionMixin,
    generics.CreateAPIView):
    queryset = TennisCourt.objects.all()
    serializer_class = TennisCourtSerializer
    pareser_classes = (MultiPartParser, FormParser)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class TennisCourtRetrieveUpdateDestroyAPIView(
    VenueOwnerPermissionMixin,
    generics.RetrieveUpdateDestroyAPIView):
    queryset = TennisCourt.objects.all()
    serializer_class = TennisCourtSerializer
    pareser_classes = (MultiPartParser, FormParser)


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
