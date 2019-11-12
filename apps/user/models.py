from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=100)
    marriage_status = models.CharField(max_length=100)
    pregnant = models.BooleanField(default=False)
    gestation = models.DateTimeField(auto_now=False, auto_now_add=False)
    sex_of_child = models.CharField(max_length=100)
