import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Account(AbstractUser, BaseModel):
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
