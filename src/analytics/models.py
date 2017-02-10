from django.db import models

from shortener.models import AppURL


class ClickEventManager(models.Manager):
    def create_event(self, appInstance):
        if isinstance(appInstance, AppURL):
            obj, created = self.get_or_create(app_url=appInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    app_url = models.OneToOneField(AppURL)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
