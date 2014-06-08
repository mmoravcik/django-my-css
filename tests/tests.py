import mock
from datetime import datetime, timedelta

from django.test import TestCase
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from my_css import models


default_storage_mock = mock.MagicMock(
    spec=default_storage, name='default_storage_mock')


@mock.patch('django.core.files.storage.default_storage._wrapped',
    default_storage_mock)
class MyCSS(TestCase):
    def test_unicode_representation(self):
        my_css = models.MyCSS.objects.create(css=' ')
        self.assertEqual(unicode(my_css), unicode(my_css.id))
        my_css.css = '  '
        my_css.save()
        my_css_archive = models.MyCSSArchive.objects.get(id=1)
        self.assertEqual(unicode(my_css_archive), unicode(my_css_archive.id))


class MyCSSFileCreation(TestCase):
    def setUp(self):
        self.initial_css = 'body {color: red}'
        self.saved_css = 'body {color: red}'
        self.default_storage_mock = mock.MagicMock(
            spec=default_storage, name='default_storage_mock')

    def tearDown(self):
        self.default_storage_mock = None

    @mock.patch('my_css.settings.MY_CSS_ROOT', '/media/')
    @mock.patch('my_css.settings.MY_CSS_FILENAME', 'my.css')
    def test_file_is_created(self):
        with mock.patch('django.core.files.storage.default_storage._wrapped',
          self.default_storage_mock):
            my_css = models.MyCSS.objects.create(css=self.initial_css)
            self.assertTrue(self.default_storage_mock.exists.called)
            self.assertEqual(self.default_storage_mock.save.call_count, 1)
            my_css.css = self.saved_css
            my_css.save()
            # TODO: workout why the following doesn't work
            # self.default_storage_mock.save.assert_called_with(
            #    '/media/my.css', ContentFile(self.saved_css))
            self.assertEqual(self.default_storage_mock.save.call_count, 2)


@mock.patch('django.core.files.storage.default_storage._wrapped',
    default_storage_mock)
class MyCSSArchiving(TestCase):
    def setUp(self):
        self.initial_css = 'body {}'
        self.saved_css = 'body {color: red}'
        self.saved_again_css = 'body {color: green}'

    def _get_my_css_archives(self):
        return models.MyCSSArchive.objects.all().order_by('id')

    def test_archive_is_not_created_for_first_css(self):
        models.MyCSS.objects.create(css=self.initial_css)

        self.assertEqual(len(self._get_my_css_archives()), 0)

    def test_arhive_is_created(self):
        my_css = models.MyCSS.objects.create(css=self.initial_css)
        my_css.css = self.saved_css
        my_css.save()

        self.assertEqual(len(self._get_my_css_archives()), 1)
        self.assertEqual(self._get_my_css_archives()[0].css, self.initial_css)

    def test_aditional_archive_is_created(self):
        my_css = models.MyCSS.objects.create(css=self.initial_css)
        my_css.css = self.saved_css
        my_css.save()
        my_css.css = self.saved_again_css
        my_css.save()

        self.assertEqual(len(self._get_my_css_archives()), 2)
        self.assertEqual(self._get_my_css_archives()[0].css, self.initial_css)
        self.assertEqual(self._get_my_css_archives()[1].css, self.saved_css)

    def test_archive_is_not_created_when_no_change_is_made(self):
        my_css = models.MyCSS.objects.create(css=self.initial_css)
        my_css.css = self.saved_css
        my_css.save()
        my_css.css = self.saved_css
        my_css.save()

        self.assertEqual(len(self._get_my_css_archives()), 1)
        self.assertEqual(self._get_my_css_archives()[0].css, self.initial_css)

    @mock.patch('my_css.settings.MY_CSS_ARCHIVE_LIFE', 0)
    def test_archive_is_not_created_when_no_needed(self):
        my_css = models.MyCSS.objects.create(css=self.initial_css)
        my_css.css = self.saved_css
        my_css.save()

        self.assertEqual(len(self._get_my_css_archives()), 0)

    @mock.patch('my_css.settings.MY_CSS_ARCHIVE_LIFE', 1)
    def test_archive_is_cleaned_up(self):
        my_css = models.MyCSS.objects.create(css=self.initial_css)
        my_css.css = self.saved_css
        my_css.save()

        self.assertEqual(len(self._get_my_css_archives()), 1)
        archive = self._get_my_css_archives()[0]
        # manually expire the archive
        archive.date_created = datetime.now() - timedelta(days=2)
        archive.save()
        my_css.css = self.saved_again_css
        my_css.save()
        self.assertEqual(len(self._get_my_css_archives()), 1)
        self.assertEqual(self._get_my_css_archives()[0].css, self.saved_css)
