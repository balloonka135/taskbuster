from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth.views import logout

from .views import home, home_files

urlpatterns = [ 
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', home_files, name='home-files'),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
]
