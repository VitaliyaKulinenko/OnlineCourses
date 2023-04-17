
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    TCH = 'Teacher'
    STD = 'Student'
    USER_CHOICES = [
        (TCH, 'Teacher'),
        (STD, 'Student'),
    ]
    owner = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name="profile")
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user_status = models.CharField(max_length=7, choices=USER_CHOICES, default=STD)

    def __str__(self):
        return self.username


@receiver(post_save, sender=User)
def create_profile(instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
