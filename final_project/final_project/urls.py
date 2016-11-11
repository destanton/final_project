from django.conf.urls import url, include
from django.contrib import admin

from sherlock.views import IndexView, UserCreateView, ProfileDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^accounts/profile/$', ProfileDetailView.as_view(), name="profile_detail_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
