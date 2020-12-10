from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy
from main.managers import CustomUserManager
from django.utils import timezone


class User(AbstractUser):

    username = None
    email = models.EmailField(ugettext_lazy('email address'), blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    NHS_no = models.CharField(max_length=10, unique=True)
    USERNAME_FIELD = 'NHS_no'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class HealthCheck(models.Model):
    age = models.SmallIntegerField()
    height = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    smoking = models.SmallIntegerField()
    alcohol = models.SmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True, default=timezone.now())

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.date}'                    