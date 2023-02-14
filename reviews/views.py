from rest_framework import generics
from .models import Review, Response
from .serializers import ReviewSerializer, ReviewListSerializer, ResponseSerializer
from api.mixins import ReviewOwnerPermissionMixin, ResponseOwnerPermissionMixin
from rest_framework.parsers import MultiPartParser, FormParser


class ReviewListAPIView(
    generics.ListAPIView,
    ReviewOwnerPermissionMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    parser_classes = (MultiPartParser, FormParser)
    

class ReviewCreateAPIView(
    generics.CreateAPIView,
    ReviewOwnerPermissionMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView,
    ReviewOwnerPermissionMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    parser_classes = (MultiPartParser, FormParser)


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ResponseListCreateAPIView(
    generics.ListCreateAPIView,
    ResponseOwnerPermissionMixin):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        return Response.objects.filter(review=self.kwargs['pk'])
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, review_id=self.kwargs['pk'])



class ResponseRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView,
    ResponseOwnerPermissionMixin):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Response.objects.filter(review=self.kwargs['pk'])

