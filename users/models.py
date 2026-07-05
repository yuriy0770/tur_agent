from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=50, verbose_name='')

    def __str__(self):
        return self.phone


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Профиль {self.user.username}'