from django.db import models
from Flavium import settings
from bookings.models import Booking
from django.contrib.contenttypes.fields import GenericRelation
from reviews.models import Review
from api.models import Images
# Create your models here.


DISTRICT_CHOICES = (
        ('OL', 'Olmazor'),
        ('BE', 'Bektemir'),
        ('YU', 'Yunusobod'),
        ('MU', 'Mirzo Ulug\'bek'),
        ('SH', 'Shayxontohur'),
        ('UC', 'Uchtepa'),
        ('CH', 'Chilonzor'), 
        ('MI', 'Mirobod'),
        ('SE', 'Sergeli'),
        ('YS', 'Yakkasaroy'),
        ('YA', 'Yashnobod'),  
        ('TV', 'Toshkent Viloyati'),
        ('ZA', 'Zangiota'),
        ('QB', 'Qibray'),
        ('BO', 'Bo\'stonliq'),
    )


class Venue(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=2, choices=DISTRICT_CHOICES)
    email = models.EmailField(blank=True,null=True)
    website = models.URLField(blank=True,null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    opens_at = models.TimeField(null=True)
    closes_at = models.TimeField(null=True)
    lights = models.BooleanField(default=True)
    indoor = models.BooleanField(default=False)
    public = models.BooleanField(default=True)
    #bookings = GenericRelation(Booking, related_query_name='%(app_label)s_%(class)s')
    ratings_count = models.IntegerField(default=0)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    users_liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='%(app_label)s_%(class)s_liked', blank=True)


    def is_public(self) -> bool:
        return self.public

    def __str__(self):
        return self.name
    class Meta:
        abstract = True



class TennisCourt(Venue):
    SURFACE_CHOICES = (
        ('H', 'Hard'),
        ('C', 'Clay'),
    )
    surface = models.CharField(max_length=1, choices=SURFACE_CHOICES)
    court_count = models.IntegerField(default=1)
    bookings = GenericRelation(Booking, related_query_name='tenniscourt')
    reviews = GenericRelation(Review, related_query_name='tenniscourt')
    images = GenericRelation(Images, related_query_name='tenniscourt')


