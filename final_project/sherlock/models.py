from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    picture = models.FileField(default='picture.png')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=25, blank=True)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    @property
    def profile_pic(self):
        if self.picture:
            return self.picture.url

    @property
    def get_year(self):
        year = self.joined.year
        return "Joined in {}".format(year)

    @property
    def get_about(self):
        return About.objects.get(user=self.user).biography


class About(models.Model):
    user = models.OneToOneField('auth.User')
    biography = models.TextField(max_length=255)

    # def __str__(self):
    #     return self.biography
