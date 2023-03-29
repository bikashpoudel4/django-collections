import os,jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
import uuid

## Creating User MANAGER using django BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, **extra_fields):
        if first_name is None:
            raise TypeError('Users must have a First Name')
        if last_name is None:
            raise TypeError('Users must have a Last Name')
        if email is None:
            raise TypeError('Users must have an email address.')
        # user = self.model(first_name=first_name, last_name=last_name, email=self.normalize_email(email),**kwargs)
        user = self.model(email=email, 
                          username=username,
                          first_name=first_name, 
                          last_name=last_name,
                          **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, first_name, last_name, mobile, password):
        if not email:
            raise ValueError('Users must have an email address.')
        user = self.create_user(
                email=self.normalize_email(email),
                username=username,
                first_name=first_name,
                last_name=last_name,
                mobile=mobile,
                is_staff=True,
                is_admin=True
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

## Users are Created Here user id is saved using UUID
class UserProfiile(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False, unique=True, editable=False,
                               max_length=500, name=("user_id"), verbose_name=("User ID"))
    # user_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    mobile = models.CharField(db_index=True, max_length=11, blank=True)
    email = models.EmailField(db_index=True, unique=True)
    city = models.CharField(db_index=True, max_length=100, blank=True)
    birth_date = models.DateField(db_index=True, blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=False)
    is_confirmed = models.BooleanField(default=False) # when otp confirmed returns True
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    # otp = models.IntegerField(editable=False, default=False) #storing otp
    otp = models.IntegerField(null=True,blank=True) # storing otp
    is_used = models.BooleanField(default=False)  # returns true if stored otp is already in use

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'mobile']

    # def __str__(self):
    #     return "{}".format(self.username)
    
    def __str__(self):
        return self.email
    
    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = 'UserProfiile'
        managed = True


