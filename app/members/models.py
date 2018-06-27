from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models

class UserManager(UserManager):
    def create_superuser(self, *args, **kwargs):
        return super().create_superuser(age=30, *args, **kwargs)

class User(AbstractUser):
    img_profile = models.ImageField(
        upload_to='user',
        blank=True
    )
    age = models.IntegerField()

    objects = UserManager()
