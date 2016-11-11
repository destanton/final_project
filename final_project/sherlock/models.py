from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    picture = models.ImageField()
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=25, blank=True)

class About(models.Model):
    biography = models.TextField(max_length=255)
    
