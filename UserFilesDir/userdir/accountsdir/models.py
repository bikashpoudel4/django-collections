import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DefaultUserManager
def user_profile_picture_path(instance, filename):
    # This function will generate the path where profile pictures are stored.
    # return os.path.join('user_profiles', str(instance.id), filename)
    return os.path.join('user_profiles', str(instance.username), filename)

def user_cover_picture_path(instance, filename):
    # This function will generate the path where cover pictures are stored.
    # return os.path.join('user_covers', str(instance.id), filename)
    return os.path.join('user_covers', str(instance.username), filename)

class UserManager(DefaultUserManager):
    pass

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    profile_picture = models.ImageField(upload_to=user_profile_picture_path, null=True, blank=True)
    cover_picture = models.ImageField(upload_to=user_cover_picture_path, null=True, blank=True)

    objects = UserManager()

    def __str__(self):
        return self.username
