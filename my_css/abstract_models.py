from datetime import datetime, timedelta

from django.db import models
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from my_css import settings


class AbstractMyCSS(models.Model):
    css = models.TextField(default="", blank=True)
    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def save(self):
        self.archive()
        super(AbstractMyCSS, self).save()
        self.create_file()
        self.clean_archive()

    def create_file(self):
        path = settings.MY_CSS_ROOT + settings.MY_CSS_FILENAME
        if default_storage.exists(path):
            default_storage.delete(path)
        default_storage.save(path, ContentFile(self.css))

    def archive(self):
        if settings.MY_CSS_ARCHIVE_LIFE:
            MyCSSArchive = models.get_model('my_css', 'MyCSSArchive')
            MyCSSArchive.objects.create(css=self.css)

    def clean_archive(self):
        MyCSSArchive = models.get_model('my_css', 'MyCSSArchive')
        MyCSSArchive.objects.filter(
            date_created__gte=datetime.now()-timedelta(
                days=settings.MY_CSS_ARCHIVE_LIFE)
        ).delete()


class AbstractMyCSSArchive(models.Model):
    css = models.TextField(default="", blank=True)
    date_created = models.DateTimeField(auto_created=True)
