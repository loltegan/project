from django.db import models
from django.contrib.auth.models import AbstractUser, Permission


class Users(AbstractUser):
    image = models.ImageField(upload_to='users_img', null=True, blank=True)


