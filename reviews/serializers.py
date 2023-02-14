from rest_framework import serializers
from .models import Review, Response
from generic_relations.relations import GenericRelatedField
from venues.models import TennisCourt
from bookings.models import Booking
from api.models import Images
from api.serializers import ImageSerializer



class ReviewListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = [
            'id', 
            'user', 
            'review_text', 
            'rating', 
            'updated_at',
            'number_of_players',
            'images',
            ]


class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    venue = GenericRelatedField(
        {TennisCourt: serializers.HyperlinkedRelatedField(
            queryset=TennisCourt.objects.all(),
            view_name='tenniscourt-detail',
            ),
        # add other venue types here
        # FootballPitch: serializers.HyperlinkedRelatedField(
        #     queryset=FootballPitch.objects.all(),
        #     view_name='footballpitch-detail',
        # ),
        }
    )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    booking = serializers.HyperlinkedRelatedField(write_only=True, queryset=Booking.objects.all(), view_name='booking-detail', required=True)
    review_text = serializers.CharField(required=False)
    rating = serializers.IntegerField(required=True)
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)
    number_of_players = serializers.IntegerField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    responses = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Review
        fields = [
            'id', 
            'user', 
            'booking',
            'venue', 
            'review_text',
            'rating',
            'images',
            'uploaded_images',
            'number_of_players',
            'updated_at',
            'responses',]

    def validate(self, data):
        # check if user is a venue owner
        if data['user'].is_venue_owner:
            
            raise serializers.ValidationError('Venue owners are not allowed to review')

        # check if booking exists
        if Booking.objects.filter(id=data['booking'].id).exists():
            # check if booking belongs to the user
            if Booking.objects.get(id=data['booking'].id).user == data['user']:
                # check if booking has been completed
                if Booking.objects.get(id=data['booking'].id).status == 'C':
                    # check if booking has been reviewed
                    try:
                        Booking.objects.get(id=data['booking'].id).review
                        raise serializers.ValidationError('Booking has already been reviewed')
                    except Review.DoesNotExist:
                        return data
                else:
                    raise serializers.ValidationError('Booking has not been completed')
            else:
                raise serializers.ValidationError('You are not allowed to review this booking')
        else:
            raise serializers.ValidationError('Booking does not exist')


    def create(self, validated_data):
        if 'uploaded_images' in validated_data:
            uploaded_images = validated_data.pop('uploaded_images')
            review = Review.objects.create(**validated_data)
            for image in uploaded_images:
                # check if image already exists
                if Images.objects.filter(image=image).exists():
                    raise serializers.ValidationError('Image already exists')
                else:
                    Images.objects.create(object=review, image=image)
            return review
        else:
            return Review.objects.create(**validated_data)


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



class ResponseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    review = serializers.HyperlinkedRelatedField(queryset=Review.objects.all(), view_name='review-detail', required=True)
    response_text = serializers.CharField(required=True)
    class Meta:
        model = Response
        fields = [
            'id', 
            'review', 
            'response_text',
            ]

    def validate(self, data):
        # check if review exists
        if Review.objects.filter(id=data['review'].id).exists():
            # check if review has been responded to
            if Review.objects.get(id=data['review'].id).response:
                raise serializers.ValidationError('Review has already been responded to')
            else:
                return data
        else:
            raise serializers.ValidationError('Review does not exist')


    def create(self, validated_data):
        return Response.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)