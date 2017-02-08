"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from shortener.views import app_redirect_view, AppCBView

# DO NOT DO
# from shortener import views
# from another_app.views import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^a/(?P<shortcode>[\w-]+)/$', app_redirect_view),
    url(r'^b/(?P<shortcode>[\w-]+)/$', AppCBView.as_view()),

    # DO NOT DO
    # url(r'^abc/$', 'shortener.views.app_redirect_view'),
    # url(r'^abc/$', views.app_redirect_view),
]
