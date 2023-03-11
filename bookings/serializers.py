from rest_framework import serializers
from generic_relations.relations import GenericRelatedField
#from api.relations import VenueObjectRelatedField
from .models import Booking
from venues.models import TennisCourt
import datetime





class BookingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
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
    date = serializers.DateField(required=True)
    start_time = serializers.TimeField(required=True)
    hours = serializers.IntegerField(required=True)
    end_time = serializers.TimeField(read_only=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model = Booking
        fields = [
            'id',
            'user',
            'venue',
            'date',
            'start_time',
            'hours',
            'end_time',
            'status',
        ]


    def validate(self, data):
        # check that the booking is not in the past
        if data['date'] < datetime.date.today():
            raise serializers.ValidationError("You can't book a venue in the past!")
        if data['date'] == datetime.date.today() and data['start_time'] < datetime.datetime.now().time():
            raise serializers.ValidationError("You can't book a venue in the past!")
        # check that the booking is not more than 30 days in advance
        if data['date'] > datetime.date.today() + datetime.timedelta(days=30):
            raise serializers.ValidationError("You can't book a venue more than 30 days in advance!")
        # check that the booking is not more than 16 hours
        if data['hours'] > 16:
            raise serializers.ValidationError("You can't book a venue for more than 16 hours!")
        # check that the booking is not less than 1 hour
        if data['hours'] < 1:
            raise serializers.ValidationError("You can't book a venue for less than 1 hour!")
        # check that the booking is not before the venue opens
        if data['start_time'] < data['venue'].opens_at:
            raise serializers.ValidationError("You can't book a venue before it opens!")
        # check that the booking is not after the venue closess
        if data['start_time'] > data['venue'].closes_at:
            raise serializers.ValidationError("You can't book a venue after it closes!")
        # check that the venue is not already booked for that time taking into account the duration of the booking
        if Booking.objects.filter(tenniscourt__name=data['venue'].name, date=data['date']).exists():
            if Booking.objects.filter(tenniscourt__name=data['venue'].name, date=data['date'], start_time=data['start_time']).exists():
                raise serializers.ValidationError("This venue is already booked for this time!")
            start_time = datetime.datetime.combine(data['date'], data['start_time'])
            end_time = start_time + datetime.timedelta(hours=data['hours'])
            # check if the duration of the booking doesn't overlap with another booking in future
            while start_time < end_time:
                start_time += datetime.timedelta(hours=1)
                if Booking.objects.filter(tenniscourt__name=data['venue'].name, date=data['date'], start_time=start_time).exists() and start_time != end_time:
                    raise serializers.ValidationError(f'This venue is already booked at {start_time.time()}')
            # check if the duration of the booking doesn't overlap with another booking in past
            start_time = datetime.datetime.combine(data['date'], data['start_time'])
            while start_time.time() > data['venue'].opens_at:
                start_time -= datetime.timedelta(hours=1)
                if Booking.objects.filter(tenniscourt__name=data['venue'].name, date=data['date'], start_time=start_time).exists():
                    prev_booking = Booking.objects.get(tenniscourt__name=data['venue'].name, date=data['date'], start_time=start_time)
                    if prev_booking.end_time > data['start_time']:
                        raise serializers.ValidationError(f'This venue is already booked from {prev_booking.start_time} to {prev_booking.end_time}')
        return data