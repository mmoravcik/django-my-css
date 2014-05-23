from datetime import datetime, timedelta

from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


class AbstractMyCSS(models.Model):
    css = models.TextField(default="", blank=True)
    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def save(self):
        super(AbstractMyCSS, self).save()
        path = settings.MY_CSS_ROOT + settings.MY_CSS_FILENAME

        if default_storage.exists(path):
            default_storage.delete(path)
        default_storage.save(path, ContentFile(self.css))

        self.archive()
        self.clean_archive()

    def archive(self):
        MyCSSArchive = models.get_model('my_css', 'MyCSSArchive')
        MyCSSArchive.objects.create(css=self.css)

    def clean_archive(self):
        MyCSSArchive = models.get_model('my_css', 'MyCSSArchive')
        MyCSSArchive.objects.delete(
            date_created__gte=datetime.now()-timedelta(days=30)
        )



class AbstractMyCSSArchive(models.Model):
    css = models.TextField(default="", blank=True)
    date_created = models.DateTimeField(auto_created=True)