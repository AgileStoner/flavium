from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import TennisCourt

@register(TennisCourt)
class TennisCourtIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = [
        'name',
        'address',
        'district',
        'description',
        'price',
        'surface',
        'indoor',
    ]