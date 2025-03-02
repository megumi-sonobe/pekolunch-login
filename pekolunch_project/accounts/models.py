from django.db import models
from django.contrib.auth.models import(
    BaseUserManager,AbstractBaseUser,PermissionsMixin
)
from django.urls import reverse_lazy


class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError('Enter Email')
        if not password:
            raise ValueError('Enter Password')
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,email,password=None):
        user = self.create_user(
            username = username,
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    
class Users(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=64,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def get_absolute_url(self):
        return reverse_lazy('accounts:home')
    
    
        
    
