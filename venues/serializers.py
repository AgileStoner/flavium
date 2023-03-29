from rest_framework import serializers

from .models import TennisCourt
from api.serializers import ImageSerializer
from api.models import Images

class TennisCourtListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = TennisCourt
        fields = [
            'id',
            'user',
            'name',
            'address',
            'district',
            'price',
            'images',
        ]



class TennisCourtSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    opens_at = serializers.TimeField(format='%H:%M')
    closes_at = serializers.TimeField(format='%H:%M')
    lights = serializers.BooleanField(default=True)
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)
    deleted_image_id = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)
    public = serializers.BooleanField(default=True)
    is_favorite = serializers.BooleanField(default=False)
    class Meta:
        model = TennisCourt
        fields = [
            'id',
            'user',
            'name',
            'address',
            'district',
            'price',
            'description',
            'opens_at',
            'closes_at',
            'surface',
            'indoor',
            'lights',
            'court_count',
            'images',
            'uploaded_images', 
            'deleted_image_id',
            'public',
            'is_favorite',
        ]

    def create(self, validated_data):
        if 'uploaded_images' in validated_data:
            uploaded_images = validated_data.pop('uploaded_images')
            venue = TennisCourt.objects.create(**validated_data)
            for image in uploaded_images:
                # check if image already exists
                if Images.objects.filter(image=image).exists():
                    raise serializers.ValidationError('Image already exists')
                else:
                    Images.objects.create(object=venue, image=image)
            return venue
        else:
            return TennisCourt.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'uploaded_images' in validated_data:
            uploaded_images = validated_data.pop('uploaded_images')
            for image in uploaded_images:
                Images.objects.create(object=instance, image=image)
        if 'deleted_image_id' in validated_data:
            deleted_image_id = validated_data.pop('deleted_image_id')
            for image_id in deleted_image_id:
                # check if image_id exists
                if Images.objects.filter(id=image_id).exists():
                    # check if image belongs to the venue
                    if Images.objects.get(id=image_id).object == instance:
                        Images.objects.get(id=image_id).delete()
                    else:
                        raise serializers.ValidationError('You are not allowed to delete this image')
                else:
                    raise serializers.ValidationError('Image does not exist')
        else:
            return super().update(instance, validated_data)
        return instance
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # check if user is authenticated
        if self.context['request'].user.is_authenticated:
            # check if venue has user in users_liked
            print(instance.users_liked.all())
            if self.context['request'].user in instance.users_liked.all():
                print("user is authenticated")
                data['is_favorite'] = True
        return data
    
