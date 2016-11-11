from django.conf.urls import url, include
from django.contrib import admin

from sherlock.views import IndexView, UserCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^$', UserCreateView.as_view(), name="user_create_view"),
]
