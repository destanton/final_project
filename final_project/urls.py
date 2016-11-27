from django.conf.urls import url, include
from django.contrib import admin

from sherlock.views import IndexView, UserCreateView, ProfileDetailView, ProfileUpdateView,\
                           AboutUpdateView, ContactUsView, SendEmailView,\
                           AboutUsView, ImageAddView, ImageUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^admin/', admin.site.urls),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^search/', include('haystack.urls'), name='haystack_search'),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^accounts/profile/(?P<pk>\d+)/$', ProfileDetailView.as_view(), name="profile_detail_view"),
    url(r'^profile/update/(?P<pk>\d+)/$', ProfileUpdateView.as_view(), name='profile_update_view'),
    url(r'^image/add/$', ImageAddView.as_view(), name='image_add_view'),
    url(r'^image/update/(?P<pk>\d+)/$', ImageUpdateView.as_view(), name='image_update_view'),
    url(r'^about/update/(?P<pk>\d+)/$', AboutUpdateView.as_view(), name='about_update_view'),
    url(r'^contact_us/$', ContactUsView.as_view(), name='contact_us_view'),
    url(r'^send_email/$', SendEmailView.as_view(), name='send_email_view'),
    url(r'^about_us/$', AboutUsView.as_view(), name="about_us_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
