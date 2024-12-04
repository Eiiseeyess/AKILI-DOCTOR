from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    '''The class that will be involved in the verification of the Account class'''

    def create_user(self, username, first_name, last_name, email, phone, gender='Male', date_of_birth=None, profile_picture=None, password=None):
        '''Regular user creation'''
        if not first_name:
            raise ValueError("A user must have a first name")
        if not last_name:
            raise ValueError("A user must have a last or second name")
        if username is None or username == "":
            username = first_name + last_name
        if not email:
            raise ValueError("A user must have an email")
        if password is None:
            raise ValueError("Users must have a valid password")

        if gender not in Account.GENDER_DICT:
            raise ValueError(f'Invalid gender: {gender}. Must be one of {list(Account.GENDER_DICT.keys())}.')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            gender=gender,
            phone=phone,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            profile_picture=profile_picture,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, phone, password=None):
        '''Create a superuser for the application'''
        user = self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            gender='Male',
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractUser):
    '''The base user class for the application'''
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    GENDER_DICT = dict(GENDER)

    username = models.CharField(max_length=150, unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone= models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=8, choices=GENDER, default='Male')
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    current_streak = models.IntegerField(default=1)
    longest_streak = models.IntegerField(default=1)  
    last_login_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    preferences = models.OneToOneField('articles.UserArticlePreference', on_delete=models.CASCADE, related_name='user_account_preferences', null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password']

    def __str__(self):
        '''String representation of the model'''
        return f"{self.first_name} - {self.last_name}"