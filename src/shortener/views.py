from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubminUrlForm
from .models import AppURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubminUrlForm()
        context = {
            "title": "URL Shortener",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubminUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("url"))

        context = {
            "title": "URL Shortener",
            "form": form
        }
        return render(request, "shortener/home.html", context)


class AppCBView(View):  # class based view CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(AppURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
