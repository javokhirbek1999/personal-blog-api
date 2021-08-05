from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext as _

class UserManager(BaseUserManager):

    def create_user(self, email, username, name, password=None, **kwargs):

        if not email:
            raise ValueError(_('Email is required'))
        
        user = self.model(email=self.normalize_email(email), username=username, name=name)

        user.set_password(password)

        user.save()

        return user
    
    def create_superuser(self, email, username, name, password):

        user = self.create_user(email=email, username=username, name=name, password=password)

        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name']

    objects = UserManager()

    def __str__(self):
        return self.email

