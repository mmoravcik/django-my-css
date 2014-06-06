import mock

from django.test import TestCase
from django.conf import settings
from django.core.files.storage import Storage

from my_css import models


storage_mock = mock.MagicMock(spec=Storage, name='StorageMock')
storage_mock.url = mock.MagicMock(name='url')
storage_mock.url.return_value = '/tmp/test1.css'


@mock.patch('django.core.files.storage.default_storage._wrapped', storage_mock)
class TestMyCSS(TestCase):
    def setUp(self):
        self.initial_css = 'body {}'
        self.resaved_css = 'body {color: red}'
        settings.MY_CSS_ARCHIVE_LIFE = 200

    def _get_my_css_archives(self):
        return models.MyCSSArchive.objects.all().order_by('id')

    def test_archive_is_created(self):
        self.assertEqual(len(self._get_my_css_archives()), 0)

        models.MyCSS.objects.create(css=self.initial_css)

        self.assertEqual(len(self._get_my_css_archives()), 1)
        self.assertEqual(self._get_my_css_archives()[0].css, '')

    def __test_additional_arhive_is_created(self):
        my_css = models.MyCSS.objects.create(css=self.initial_css)
        my_css.css = self.resaved_css
        my_css.save()

        self.assertEqual(len(self._get_my_css_archives()), 2)
        self.assertEqual(self._get_my_css_archives()[1].css, self.initial_css)
