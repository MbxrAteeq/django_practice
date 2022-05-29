from django.contrib.auth.models import AbstractUser
from django.db import models
from common.base_model import BaseModel


class User(AbstractUser, BaseModel):
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
