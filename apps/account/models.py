from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='media/% Y/% m/% d/', default='media/ava.png')
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    hide_age = models.BooleanField(default=False)
    city = models.CharField(max_length=100, null=True, blank=True)
    marriage_status = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
