from django.conf import settings
from django.db import models


class Follower(models.Model):
    """Модель подписчиков"""

    # то на которого хотим подписаться
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    #тот  который аторизован
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribers')

