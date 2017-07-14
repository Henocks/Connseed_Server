
from django.conf.urls import url, include
from django.contrib import admin

from Web.views import *

urlpatterns = [

    url(r'^account', Account),
    url(r'^analysis', Analysis),
    url(r'^device', Device),
    url(r'^monitoring', Monitoring),
    url(r'$', MainPage),
]