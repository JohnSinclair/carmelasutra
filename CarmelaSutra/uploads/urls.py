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
    url(r'^cv/', views.view_cv, name='view-cv'),
    url(r'^collection/(?P<pk>[0-9]+)', views.view_pic_collection, name='view-pic-collection'),
    url(r'^gallery/(?P<pk>[0-9]+)', views.view_gallery, name='view-gallery'),
   
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)),]