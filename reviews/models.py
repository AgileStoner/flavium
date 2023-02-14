from django.db import models
from Flavium.settings import AUTH_USER_MODEL as User
from bookings.models import Booking
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from api.models import Images
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ('venues', 'tenniscourt')}, null=True)
    object_id = models.PositiveIntegerField(null=True)
    venue = GenericForeignKey('content_type', 'object_id')
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    review_text = models.TextField(null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)
    number_of_players = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = GenericRelation(Images, related_query_name='tenniscourt')



    def __str__(self):
        try:
            return str(self.user) + " " + str(self.venue) + " " + str(self.rating)
        except:
            return self.review_text


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    response_text = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            return str(self.user) + " " + self.response_text
        except:
            return self.response_text




@receiver(post_save, sender=Review)
def update_average_rating(sender, instance, created, **kwargs):
    if created:
        venue = instance.venue
        venue.average_rating = (venue.average_rating * venue.ratings_count + instance.rating) / (venue.ratings_count + 1)
        venue.ratings_count += 1
        venue.save()


@receiver(post_delete, sender=Review)
def update_average_rating_delete(sender, instance, **kwargs):
    venue = instance.venue
    venue.average_rating = (venue.average_rating * venue.ratings_count - instance.rating) / (venue.ratings_count - 1)
    venue.ratings_count -= 1
    venue.save()