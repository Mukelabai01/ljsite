from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('username', 'email')
        verbose_name = 'user'
        verbose_name_plural = 'users'

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='user',
    )

    def __str__(self):
        return self.username