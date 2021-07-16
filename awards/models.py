from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
      profile_picture = CloudinaryField('image')
      bio = models.TextField(max_length=500, default="My Bio", blank=True)
      contact = models.CharField(max_length=60,blank=True)
      timestamp = models.DateTimeField(default=timezone.now())
 


class Project(models.Model):
    title = models.CharField(max_length=60,blank=True)
    image = CloudinaryField('image')
    description = models.TextField(max_length=500)
    link = models.URLField(blank=True)
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    REVIEW_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
    usability = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
    content = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
    average =  models.DecimalField(default=1,blank=False,decimal_places=2,max_digits=40)
    project = models.ForeignKey(Project,null=True,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)