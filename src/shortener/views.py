from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def app_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view FBV
    # print(request.user)
    # print(request.user.is_authenticated())
    return HttpResponse("hello {}".format(shortcode))


class AppCBView(View):  # class based view CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse("hello again {}".format(shortcode))
