from django.contrib.auth.models import AbstractUser
from django.db import models


class UserNet(AbstractUser):
    """ Custom user model    """

    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    social = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    users_media = models.ManyToManyField('UsersMedia', related_name='users')


class UsersMedia(models.Model):
    """ Users_media  """
    name = models.CharField(max_length=100)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, max_length=20)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=20)
    ref = models.URLField(max_length=300)
    file = models.FileField(null=True, blank=True)
    name_users = models.ManyToManyField(UserNet, related_name='users')

    def __str__(self):
        return self.name
