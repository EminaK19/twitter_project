import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models, transaction
from django.utils import timezone



class UserManager(models.Manager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        
        with transaction.atomic():
            user = self.model(email=email, **extra_fields) # user = MyUser(email='hhh.mail.ru', password='12323')  user.save()
            user.set_password(password)
            user.generate_activation_code()
            user.save(using=self._db)
            return user
        

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        user = self._create_user(
            username,
            email,
            password=password,
            **extra_fields
        )        
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        user = self._create_user(
            username,
            email,
            password=password,
            **extra_fields
        )
        return user 

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})


class User(AbstractBaseUser, PermissionsMixin):
    username        = models.CharField(max_length=70, unique=True)
    email           = models.EmailField(max_length=50,unique=True)
    first_name      = models.CharField(max_length=50, default='')
    last_name       = models.CharField(max_length=60, default='')
    date_joined     = models.DateTimeField(default=timezone.now)
    is_active       = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=36, blank=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    object = UserManager()

    # def __str__(self):
    #     return self.username

    def generate_activation_code(self):
        code = str(uuid.uuid4())
        self.activation_code = code

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name
    
    @property
    def user_permission(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     return self.is_staff

    # @property
    # def is_superuser(self):
    #     "Is the user a admin member?"
    #     return self.is_superuser

    # @property
    # def is_active(self):
    #     "Is the user active?"
    #     return self.is_active






