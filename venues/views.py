from rest_framework import generics
from .serializers import TennisCourtSerializer, TennisCourtListSerializer
from .models import TennisCourt
from api.mixins import VenueOwnerPermissionMixin
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import DISTRICT_CHOICES



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



class SearchListView(generics.GenericAPIView):
    queryset = TennisCourt.objects.all()
    serializer_class = TennisCourtListSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        search = request.GET.get('q')
        if search:
            # if search starts with 'district', filter by the word after 'district'
            if search.startswith('district'):
                district = search.split('district')[1].strip()
                print("FUCK")
                print(district)
                if district in [district[0] for district in DISTRICT_CHOICES]:
                    queryset = queryset.filter(district=district)
            else:
                queryset = queryset.filter(name__icontains=search)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
