from django.db import models
from Flavium.settings import AUTH_USER_MODEL
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from datetime import timedelta
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from knox.models import AuthToken as Token
#from django_q.tasks import async_task



# Create your models here.

STATUS_CHOICES = (
    ('A', 'Accepted'),
    ('R', 'Rejected'),
    ('F', 'Finished'),
    ('C', 'Cancelled'),
)

class Booking(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ('venues', 'tenniscourt')})
    object_id = models.PositiveIntegerField()
    venue = GenericForeignKey('content_type', 'object_id')
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    hours = models.IntegerField(null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    notes = models.TextField(blank = True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    @property
    def total_price(self):
        return self.venue.price * self.hours

    @property
    def end_time(self):
        return (datetime.combine(self.date, self.start_time) + timedelta(hours=self.hours)).time()

    def __str__(self):
        try:
            return self.venue.name + ' | ' + str(self.date) + ' | ' + str(self.start_time) + ' | Hours: ' + str(self.hours) 
        except:
            return self.venue.name + ' | ' + self.status
# sender is the knox Token model
@receiver(post_save, sender=Token)
def update_bookings(sender, instance, **kwargs):
    user = instance.user
    bookings = Booking.objects.filter(user=user, status='A')
    for booking in bookings:
        if booking.end_time < datetime.now().time() and booking.date <= datetime.now().date():
            booking.status = 'F'
            booking.save()
            # Need to add code to ask user to rate the venue
            


#async_task('bookings.tasks.update_bookings', schedule='H')