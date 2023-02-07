from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import *
from django.core.exceptions import ValidationError



def ValidMail(Value):
    if not str(Value).endswith('@esprit.tn'):
        raise ValidationError('mail must end with this expression')
    return Value


def LenValid(Value):
    if len(Value)!=8 :
        raise ValidationError("la longeur doit etre plus ptitttt a 8")
    return Value


class Person(AbstractUser):
    cin = models.CharField(
        "CIN",
        primary_key=True,
        max_length=8,
validators=[MinLengthValidator(8,message='la longeur doit etre min a 8 ')]
    )
    username = models.CharField("Username", max_length=255, unique=True)
    email = models.EmailField(
        unique=True,validators=[ValidMail]
    )

    USERNAME_FIELD = 'username'
