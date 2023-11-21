from form_app.models import Form
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


# this can be a superuser or a normal user
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# after creating the basic user and verifying the email we check for payment
class Appliers(models.Model):
    class StatusChoices(models.TextChoices):
        PAID = 'PD', 'PAID'
        PENDING = 'P', 'PENDING'
        FAILED = 'F', 'FAILED'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices,default=StatusChoices.PENDING)
