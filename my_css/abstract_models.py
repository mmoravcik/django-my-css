from datetime import datetime, timedelta

from django.db import models
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.db.models.signals import pre_save
from django.dispatch import receiver

from my_css import settings


class AbstractMyCSS(models.Model):
    css = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return str(self.id)

    # def save(self, *args, **kwargs):
    #     super(AbstractMyCSS, self).save(*args, **kwargs)
    #     self.create_file()
    #     self.clean_archive()
        #self.archive(old_instance.css)

    def create_file(self):
        path = settings.MY_CSS_ROOT + settings.MY_CSS_FILENAME
        if default_storage.exists(path):
            default_storage.delete(path)
        default_storage.save(path, ContentFile(self.css))

    def archive(self, original_css):
        if settings.MY_CSS_ARCHIVE_LIFE:
            MyCSSArchive = models.get_model('my_css', 'MyCSSArchive')
            my_css_archive = MyCSSArchive.objects.create(css=original_css)

    def clean_archive(self):
        MyCSSArchive = models.get_model('my_css', 'MyCSSArchive')
        MyCSSArchive.objects.filter(
            date_created__gte=datetime.now()-timedelta(
                days=settings.MY_CSS_ARCHIVE_LIFE)
        ).delete()


class AbstractMyCSSArchive(models.Model):
    css = models.TextField(blank=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return str(self.id)

