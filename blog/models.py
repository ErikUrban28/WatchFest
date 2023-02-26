from django.apps import apps
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext as _


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, login, email, password, **extra_fields):
        if not login:
            raise ValueError("The given login must be set")

        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        login = GlobalUserModel.normalize_username(login)
        user = self.model(login=login, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        if not password:
            raise ValueError("The given password must be set")
        if not email:
            raise ValueError("The given email must be set")
        return self._create_user(login, email, password, **extra_fields)

    def create_superuser(self, login, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(login, email, password, **extra_fields)


class CustomUser(AbstractUser):
    username, first_name, last_name = None, None, None
    login = models.CharField(max_length=30, unique=True, validators=[UnicodeUsernameValidator()],
                             error_messages={
                                 "unique": _("A user with that username already exists."),
                             }, )
    email = models.EmailField(blank=True,)
    password = models.CharField(_("password"), max_length=34)

    USERNAME_FIELD = 'login'
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.login


class Article(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    img = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-articles')
