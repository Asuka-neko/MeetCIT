from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return self.email