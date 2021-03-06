from datetime import datetime, timedelta

from django.db import models
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from my_css import settings


class AbstractMyCSS(models.Model):
    css = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s" % self.id

    def save(self, *args, **kwargs):
        if self.id:
            MyCSS = models.get_model('my_css', 'MyCSS')
            my_css_original = MyCSS.objects.get(id=self.id)
            if not self.css == my_css_original.css:
                my_css_original.archive()
        super(AbstractMyCSS, self).save(*args, **kwargs)
        self.create_file()
        self.clean_archive()

    def create_file(self):
        self.path = settings.MY_CSS_ROOT + settings.MY_CSS_FILENAME
        if default_storage.exists(self.path):
            default_storage.delete(self.path)
        default_storage.save(self.path, ContentFile(self.css))

    def archive(self):
        if settings.MY_CSS_ARCHIVE_LIFE:
            MyCSSArchive = models.get_model('my_css', 'MyCSSArchive')
            MyCSSArchive.objects.create(css=self.css)

    def clean_archive(self):
        MyCSSArchive = models.get_model('my_css', 'MyCSSArchive')
        MyCSSArchive.objects.filter(
            date_created__lt=datetime.now()-timedelta(
                days=settings.MY_CSS_ARCHIVE_LIFE+1)
        ).delete()


class AbstractMyCSSArchive(models.Model):
    css = models.TextField(blank=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return str(self.id)
