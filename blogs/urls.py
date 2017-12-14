from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from blogs.views import home, register, blog_detail

urlpatterns = [
    url(r'^$', home),
    url(r'^register/$', register),
    url(r'^blog_detail/$', blog_detail),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

