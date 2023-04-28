from rest_framework import generics
from .serializers import TennisCourtSerializer, TennisCourtListSerializer, TennisCourtCreateSerializer, TennisCourtUpdateSerializer
from .models import TennisCourt
from api.mixins import VenueOwnerPermissionMixin
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import DISTRICT_CHOICES
from bookings.models import Booking
from datetime import datetime
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated



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
    serializer_class = TennisCourtCreateSerializer
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


class TennisCourtUpdateAPIView(
    generics.UpdateAPIView):
    queryset = TennisCourt.objects.all()
    serializer_class = TennisCourtUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)





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
                if district in [district[0] for district in DISTRICT_CHOICES]:
                    queryset = queryset.filter(district=district)
            elif search.startswith('surface'):
                surface = search.split('surface')[1].strip()
                if surface in ['H', 'C']:
                    queryset = queryset.filter(surface=surface)
            elif search.startswith('indoor'):
                indoor = search.split('indoor')[1].strip()
                if indoor in ['True', 'False']:
                    queryset = queryset.filter(indoor=indoor)
            elif search.startswith('lights'):
                lights = search.split('lights')[1].strip()
                if lights in ['True', 'False']:
                    queryset = queryset.filter(lights=lights)
            elif search.startswith('datetime'):
                datetime_str = search.split('datetime')[1].strip()
                datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                date_obj = datetime_obj.date()
                time_obj = datetime_obj.time()
                queryset = queryset.exclude(bookings__date=date_obj, bookings__start_time=time_obj)
            elif search.startswith('date'):
                date_str = search.split('date')[1].strip()
                date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
                # exlude courts that have more than 12 bookings on that day
                queryset = queryset.annotate(num_bookings=Count('bookings')).exclude(bookings__date=date_obj, num_bookings=12)
            elif search.startswith('time'):
                time_str = search.split('time')[1].strip()
                time_obj = datetime.strptime(time_str, '%H:%M:%S').time()
                queryset = queryset.exclude(bookings__start_time=time_obj)
            else:
                queryset = queryset.filter(name__icontains=search)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
