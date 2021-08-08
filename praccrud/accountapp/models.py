# 표준 라이브러리 모듈(파이썬 or 장고 기본 모듈)
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, nickname, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, nickname, password=None):
        """Create a new superuser"""
        user = self.create_user(email, name=name, nickname=nickname, password=password,)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class MyUser(AbstractBaseUser):
    # verbose_name: email 필드값 입력창에 대한 설명을 나타낸다.
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email' # email 필드를 고유식별자로 취급(pk), 기본제공 모델에서는 username이 pk
    REQUIRED_FIELD = ['name', 'nickname'] # 항상 값이 가져야 하는 필드 지정

    # 이메일 값을 문자열 값으로 리턴한다.
    def __str__(self):
        return self.email

    # first name + last name
    def get_full_name(self):
        return self.name

    # first name only
    def get_short_name(self):
        return self.name