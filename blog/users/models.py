from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email=models.EmailField(unique=True)

    # cambio el username por el email.
    # si realizo un cambio de superuser debo comentar estas lineas.
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
