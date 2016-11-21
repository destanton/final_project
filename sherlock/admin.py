from django.contrib import admin

from sherlock.models import Profile, About, Relative

admin.site.register([Profile, About, Relative])
