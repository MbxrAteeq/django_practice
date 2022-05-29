import datetime
from django.db import models
from django.utils.translation import gettext as _
from app.models import User
from common.base_model import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
