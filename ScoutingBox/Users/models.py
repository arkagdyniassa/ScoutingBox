from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User, AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        """Create and save a User with the given email and password."""

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):

        """Create and save a regular User with the given email and password."""

        extra_fields.setdefault('is_staff', False)

        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        """Create and save a SuperUser with the given email and password."""

        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class UserData(AbstractUser):

    username = None

    email = models.EmailField(('user email'), unique=True, null=False)

    phone_number = models.CharField(verbose_name=('phone number'), max_length=17)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

# w settings wskaż na ten model jako AUTH_USER_MODEL = 'user.User'
