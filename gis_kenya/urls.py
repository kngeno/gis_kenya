from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()
   
urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'core.views.home', name='home'),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'core/cover.html'}, name='login'),
    url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),    
    url(r'^signup/$', 'auth.views.signup', name='signup'),

    url(r'^settings/$', 'core.views.settings', name='settings'),
    url(r'^settings/picture/$', 'core.views.picture', name='picture'),
    url(r'^settings/upload_picture/$', 'core.views.upload_picture', name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', 'core.views.save_uploaded_picture', name='save_uploaded_picture'),
    url(r'^settings/password/$', 'core.views.password', name='password'),

    url(r'^network/$', 'core.views.network', name='network'),
    url(r'^feeds/', include('feeds.urls')),
    url(r'^questions/', include('questions.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^messages/', include('messages.urls')),

    url(r'^notifications/$', 'activities.views.notifications', name='notifications'),
    url(r'^notifications/last/$', 'activities.views.last_notifications', name='last_notifications'),
    url(r'^notifications/check/$', 'activities.views.check_notifications', name='check_notifications'),
    
    url(r'^search/$', 'search.views.search', name='search'),
    url(r'^(?P<username>[^/]+)/$', 'core.views.profile', name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
