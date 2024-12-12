from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class AdvUser(AbstractUser):
    its_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошёл активацию?')
    send_messages = models.BooleanField(default=True, verbose_name = 'Слать оповещение о новых комментариях?')
class Meta(AbstractUser.Meta):
    pass