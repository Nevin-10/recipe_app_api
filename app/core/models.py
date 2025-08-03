"""
DATABASE MODELS
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """Manager For USERS"""
    def create_user(self, email, password=None, **extra_fields):
        """Create, Save and return USER"""
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # self.model is part of BaseUserManager
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return SUPERUSER"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        # Fields provided by PermissionsMixin(is_superuser)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """USER IN THE SYSTEM"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
