from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User)