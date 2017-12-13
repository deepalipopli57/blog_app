from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('blogs.urls')),
    url(r'^logout/$', auth_views.logout),
    url(r'^login/$', auth_views.login),
]

