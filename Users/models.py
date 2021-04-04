from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _




class CustomAccountManager(BaseUserManager):

    def create_user(self, email, username, password, is_verified):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have an username")
        if not password:
            raise ValueError("User must have an password")

        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.is_admin = False
        user.is_staff = False
        user.is_superuser = False
        user.is_verified = False
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have an username")
        if not password:
            raise ValueError("User must have an password")

        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.is_verified = False
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=20, unique=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


    objects = CustomAccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
