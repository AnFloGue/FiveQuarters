# account/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.hashers import make_password

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None, user_type='franchise_owner'):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            user_type='inventory_manager'
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    USER_TYPES = (
        ('inventory_manager', 'Inventory Manager'),
        ('franchise_owner', 'Franchise Owner'),
    )
    email = models.EmailField(max_length=100, unique=True, primary_key=True)
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    is_suspended = models.BooleanField(default=True)
    suspended_at = models.DateTimeField(blank=True, null=True)
    resumed_at = models.DateTimeField(blank=True, null=True)
    suspended_description = models.TextField(blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='franchise_owner')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def save(self, *args, **kwargs):
        if not self.pk or self._state.adding or 'password' in self.get_deferred_fields():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10, default='00000')
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def user_type(self):
        return self.user.user_type