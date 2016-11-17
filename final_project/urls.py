from django.conf.urls import url, include
from django.contrib import admin

from sherlock.views import IndexView, UserCreateView, ProfileDetailView, ProfileUpdateView,\
                           AboutUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('haystack.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^accounts/profile/(?P<pk>\d+)/$', ProfileDetailView.as_view(), name="profile_detail_view"),
    url(r'^profile/update/(?P<pk>\d+)/$', ProfileUpdateView.as_view(), name='profile_update_view'),
    url(r'^about/update/(?P<pk>\d+)/$', AboutUpdateView.as_view(), name='about_update_view'),
    # url(r'^searching/?$', AboutSearchView.as_view(), name="about_search_view"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
