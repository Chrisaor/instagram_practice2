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
    age = models.IntegerField('나이')
    like_posts = models.ManyToManyField(
        'posts.Post',
        verbose_name='좋아요 누른 포스트 목록'
    )

    objects = UserManager()
    
    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = f'{verbose_name} 목록'
