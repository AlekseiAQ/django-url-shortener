from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def app_redirect_view(request, *args, **kwargs):  # function based view FBV
    return HttpResponse("hello")


class AppCBView(View):  # class based view CBV
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello again")
