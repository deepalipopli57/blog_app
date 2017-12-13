from django.conf.urls import url
from blogs.views import home, register

urlpatterns = [
    url(r'^$', home),
    url(r'^register/$', register),

]