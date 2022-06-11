from django.db import models

# Create your models here.

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.db import connection


ROLE_CHOICES = (
    ("Applicant", "Applicant"),
    ('Recruiter', "Recruiter"),
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email,  password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.TextField(max_length=200,default="Rafik Bhai Shaikh",null=True,blank=True)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(max_length=40,choices=ROLE_CHOICES, default="Applicant")
    
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']
    # def __str__(self):
    #     return self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    

# class Profile(models.Model) :
    
#     fullname = models.CharField(max_length=200,null=True,blank=True)
#     degree = models.CharField(max_length=200,null=True,blank=True)
#     email = models.EmailField(max_length=200,null=True,blank=True)
#     contact_no = models.CharField(max_length=200,null=True,blank=True)
#     date_of_birth = models.DateField(null=True,blank=True)
#     NID_no = models.CharField(max_length=200,null=True,blank=True)    
    
    
#     created_by = models.OneToOneField(MyUser,on_delete=models.CASCADE,null=False,blank=False)
    
    
    