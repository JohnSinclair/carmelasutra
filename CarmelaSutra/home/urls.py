from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.views import static
# import django_cas_ng.views
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', views.index, name='index'),
    
   
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)),]