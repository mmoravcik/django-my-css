from django.db.models import get_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

MyCSS = get_model('my_css', 'MyCSS')


@receiver(pre_save, sender=MyCSS)
def my_css_presave_handler(sender, **kwargs):
    import ipdb;ipdb.set_trace()
    kwargs['instance'].archive(kwargs['instance'].css)