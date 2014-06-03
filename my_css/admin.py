from django.db.models import get_model
from django.contrib import admin

MyCSS = get_model('my_css', 'MyCSS')
MyCSSArchive = get_model('my_css', 'MyCSSArchive')


admin.site.register(MyCSS)
admin.site.register(MyCSSArchive)