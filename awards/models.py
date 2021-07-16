from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
      profile_picture = CloudinaryField('image')
      bio = models.TextField(max_length=500, default="My Bio", blank=True)
      contact = models.CharField(max_length=60,blank=True)
      timestamp = models.DateTimeField(default=timezone.now())
 