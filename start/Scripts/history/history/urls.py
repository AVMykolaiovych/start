"""history URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from django.conf.urls import include

from django.contrib import admin

# from post import views

from post.views import (
    posthome,
    postcreate,
    postdetail,
    postlist,
    postupdate,
    postdelete,
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/$', posthome),
    url(r'^create/$', postcreate),
    # url(r'^detail/$', postdetail),
    url(r'^detail/$', postdetail),
    url(r'^update/$', postupdate),
    url(r'^delete/$', postdelete),
    url(r'^$', postlist),
]
