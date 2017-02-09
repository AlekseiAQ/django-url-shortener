from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import AppURL


def app_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view FBV
    obj = get_object_or_404(AppURL, shortcode=shortcode)
    return HttpResponse("hello {}".format(obj.url))


class AppCBView(View):  # class based view CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(AppURL, shortcode=shortcode)
        return HttpResponse("hello again {}".format(shortcode))

    def post(self, request, *args, **kwargs):
        return HttpResponse()


"""
def app_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view FBV
# print(request.user)
# print(request.user.is_authenticated())
# obj = AppURL.objects.get(shortcode=shortcode)

obj = get_object_or_404(AppURL, shortcode=shortcode)
# obj_url = obj.url
# try:
#     obj = AppURL.objects.get(shortcode=shortcode)
# except:
#     obj = AppURL.objects.all().first()
# obj_url = None
# qs = AppURL.objects.filter(shortcode__iexact=shortcode.upper())
# if qs.exists() and qs.count() == 1:
#     obj = qs.first()
#     obj_url = obj.url
"""
