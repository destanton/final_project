from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)
        About.objects.create(user=instance)


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
        return 'Joined in {}'.format(year)

    @property
    def get_about(self):
        return About.objects.filter(user=self.user)


GENDER = [
    ('M', 'Male'),
    ('F', 'Female')
]

BLACK = 'blk'
BLUE = 'blu'
BROWN = 'bro'
GRAY = 'gry'
GREEN = 'grn'
HAZEL = 'hzl'
OTHER = 'oth'

EYE_COLOR = [
    (BLACK, 'Black'),
    (BLUE, 'Blue'),
    (BROWN, 'Brown'),
    (GRAY, 'Gray'),
    (GREEN, 'Green'),
    (HAZEL, 'Hazel'),
    (OTHER, 'Other')


]

COUSIN = 'csn'
CHILD = 'cld'
PARENT = 'prt'
SIBLING = 'sbl'

FAMILY = [
    (COUSIN, 'Cousin'),
    (CHILD, 'Child'),
    (PARENT, 'Parent'),
    (SIBLING, 'Sibling')
]


class About(models.Model):
    user = models.OneToOneField('auth.User')
    biography = models.TextField(max_length=255)
    birthdate = models.DateField(null=True)
    city_of_birth = models.CharField(max_length=255, blank=True)
    state_of_birth = models.CharField(max_length=150, blank=True)
    country_of_birth = models.CharField(max_length=255, blank=True)
    sex_at_birth = models.CharField(max_length=1, choices=GENDER)
    eye_color = models.CharField(max_length=3, choices=EYE_COLOR)
    mother_first_name = models.CharField(max_length=150, blank=True)
    mother_maiden_name = models.CharField(max_length=150, blank=True)
    mother_last_name = models.CharField(max_length=150, blank=True)
    father_first_name = models.CharField(max_length=150, blank=True)
    father_last_name = models.CharField(max_length=150, blank=True)
    birth_hospital = models.CharField(max_length=150, blank=True)
    searching_for = models.CharField(max_length=3, choices=FAMILY)

    # def __str__(self):
    #     return self.biography
