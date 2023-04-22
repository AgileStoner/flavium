from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Images(models.Model):
    def upload_to(instance, filename):
        return 'images/{0}/{1}'.format(instance.content_type, filename)

    image = models.ImageField(upload_to=upload_to)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    object = GenericForeignKey('content_type', 'object_id')
    def __str__(self):
        return self.image.urls