from rest_framework import serializers
from .models import Images


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField()
    class Meta:
        model = Images
        fields = [
            'id',
            'image',
        ]
    def validate(self, attrs):
        if attrs['object'].user != self.context['request'].user:
            raise serializers.ValidationError('You are not allowed to add images to this venue')
        return attrs