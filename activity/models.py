from django.db import models
from django.contrib.auth.models import AbstractUser,Permission as AuthPermission,Group as AuthGroup
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User


class User(AbstractUser):
    ACTIVITY_CHOICES = (
        ('education', 'Education'),
        ('recreational', 'Recreational'),
        ('social', 'Social'),
        ('diy', 'DIY'),
        ('charity', 'Charity'),
        ('cooking', 'Cooking'),
        ('relaxation', 'Relaxation'),
        ('music', 'Music'),
        ('busywork', 'Busywork'),
    )
    
    selected_activity = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)


    def __str__(self):
        return self.username

# Activity model
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="activities")
    activity_name = models.CharField(max_length=100,null=True,blank=True)
    # Add more fields as per your requirements
    created_at = models.DateTimeField(auto_now_add=True, blank= True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    
    def __str__(self):
        return self.activity_name
