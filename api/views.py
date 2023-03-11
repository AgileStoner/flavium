from django.shortcuts import render

# Create your views here.
from .models import Images
from .serializers import ImageSerializer
from rest_framework import generics
import os
from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.http import JsonResponse

class ImageListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        directory = 'images/districts'  # Hardcoded directory path
        path = os.path.join(settings.MEDIA_ROOT, directory)
        image_urls = []
        for filename in os.listdir(path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                image_url = request.build_absolute_uri(settings.MEDIA_URL + os.path.join(directory, filename))
                image_urls.append(image_url)
        return JsonResponse({'image_urls': image_urls})


