from rest_framework import generics
from rest_framework.response import Response
from .import client

from venues.models import TennisCourt
from venues.serializers import TennisCourtSerializer


class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if not query:
            return Response({'error': 'Please provide a search query'}, status=400)
        results = client.perform_search(query)
        return Response(results)