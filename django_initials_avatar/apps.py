from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class DjangoInitialsAvatarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_initials_avatar'
    verbose_name = _("Initials Avatar")
