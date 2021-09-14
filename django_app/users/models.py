import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):

    class Role(models.IntegerChoices):
        ADMIN = 1 , _('Administrator') 
        STAFF =  2, _('Staff') 
        STUDENT = 3, _('Student') 
        PARTNER =  4, _('Partner') 
        USER =  5, _('User') 

    email = models.EmailField(_('email address'), unique=True)
    uuid = models.UUIDField(_('uuid'), default=uuid.uuid4, editable=False)
    name = models.CharField(_('name'), blank=True, max_length=30)
    role = models.PositiveSmallIntegerField(_('role'), choices=Role.choices, default=Role.USER)
    is_staff = models.BooleanField(_('is staff'), default=False)
    is_active = models.BooleanField(_('is active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email
