from django.contrib.admin.utils import help_text_for_field
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    age = models.IntegerField(blank=True, null=True, max_length=3)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    personal_code = models.CharField(max_length=10)
    father_phone_number = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.username}"

