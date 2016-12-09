from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm


class Services(models.Model):
    service_name = models.CharField(max_length=512)
    url = models.CharField(max_length=512)
    icon = models.CharField(max_length=512)
    is_visible = models.BooleanField()

    def __unicode__(self):
        return '%s : %s' % (self.service_name, self.url)

    def get_url(self):
        return self.url

    class Meta:
        managed = True
        db_table = 'services'


class General (models.Model):
    title = models.CharField(max_length=512)

    def __unicode__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'general'


class Drives (models.Model):
    letter = models.CharField(max_length=128)

    def __unicode__(self):
        return self.letter

    class Meta:
        managed = True
        db_table = 'drives'
