import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models, transaction
from django.utils import timezone



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff = False, is_admin = False):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff  = is_staff
        user_obj.admin  = is_admin
        user_obj.active = is_active 
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_admin =True
        )
        return user 


class User(AbstractBaseUser, PermissionsMixin):
    username        = models.CharField(max_length=70)
    email           = models.EmailField(max_length=50,unique=True)
    first_name      = models.CharField(max_length=50, default='')
    last_name       = models.CharField(max_length=60, default='')
    date_joined     = models.DateTimeField(default=timezone.now)
    active       = models.BooleanField(default=True)
    staff        = models.BooleanField(default=False)
    admin        = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=36, blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def generate_activation_code(self):
        code = str(uuid.uuid4())
        self.activation_code = code

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active



# class Profile(models.Model):
#     # adds extra data
#     user      = models.OneToOneField(User)
#     birthdate = models.DateField()
    # image     = models.ImageField()
    # city      = models.ImageField


