from django.db import models


class AppURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)
    # shortcode = models.CharField(max_length=15, null=True) Empty in database is okay
    # shortcode = models.CharField(max_length=15, default='appdefaultshortcode')

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
