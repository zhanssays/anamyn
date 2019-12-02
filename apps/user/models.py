from django.db import models


class Profile(models.Model):
    photo = models.ImageField(upload_to='media/% Y/% m/% d/', default='media/ava.png')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(auto_now=False, auto_now_add=False)
    not_show_age = models.BooleanField(default=False)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=100)
    marriage_status = models.CharField(max_length=100)
