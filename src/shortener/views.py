from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import AppURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})

    def post(self, request, *args, **kwargs):
        # some_dict = {}
        # some_dict.get("url", "http://google.com")
        print(request.POST.get("url"))
        return render(request, "shortener/home.html", {})


class AppCBView(View):  # class based view CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(AppURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
