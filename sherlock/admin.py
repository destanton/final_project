from django.contrib import admin

from sherlock.models import Profile, About, Relative, Image

admin.site.register([Profile, About, Relative, Image])
