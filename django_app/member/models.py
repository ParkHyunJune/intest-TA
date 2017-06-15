from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# setting AUTH_USER_MODEL을 수정해야하기 때문이 동적으로 해야한다

class User(AbstractUser):
    pass