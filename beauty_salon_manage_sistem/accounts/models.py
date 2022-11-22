from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.db import models
from django.db.models import CASCADE, PROTECT

from beauty_salon_manage_sistem.accounts.managers import AppBaseUserManager
from beauty_salon_manage_sistem.core.validators import validate_only_letters


class AppBaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppBaseUserManager()

    @property
    def get_full_name_with_profile(self):
        profile_full_name = AppStaffProfile.objects.get(pk=self.pk).get_full_name
        if profile_full_name:
            return f'{profile_full_name}'
        return 'No name'

    def __str__(self):
        return self.get_full_name_with_profile


class AppStaffProfile(models.Model):
    user = models.OneToOneField(AppBaseUser, primary_key=True, on_delete=CASCADE, )

    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 40

    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 40

    MAX_LEN_POSITION = 100

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        ]
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        ]
    )

    position = models.CharField(
        max_length=MAX_LEN_POSITION,
        null=False,
        blank=False,
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.get_full_name} - {self.position}'

    class Meta:
        verbose_name = 'Staff'


class AppCustomerUser(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 40

    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 40

    MAX_LEN_PHONE_NUMBER = len('+359888888888')
    MIN_LEN_PHONE_NUMBER = len('+359888888888')
    #
    # TODO Make it with enumerate!
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show'), ]
    MAX_LEN_GENDER = len('Do not show')
    #
    HAIR_TYPES_CHOICES = [
        ('Straight hair', 'Straight hair'),
        ('Wavy hair', 'Wavy hair'),
        ('Curly hair', 'Curly hair'),
        ('Kinky hair', 'Kinky hair'),
        ('I am not sure', 'I am not sure'),
    ]

    MAX_LEN_HAIR_TYPES = len('I am not sure')

    HAIR_LONG_CHOICES = [
        ('Short hair', 'Short hair'),
        ('Middle hair', 'Middle hair'),
        ('Long hair', 'Long hair'),
        ('Very long hair', 'Very long hair'),
        ('I am not sure', 'I am not sure'),
    ]
    MAX_LEN_HAIR_LONG = len('Very long hair')

    MAX_LEN_FURTHER_EXPLANATION = 250

    hair_stylist = models.ManyToManyField(AppBaseUser)

    choose_hair_stylist = models.CharField(
        max_length=300,
        choices=[('person.get_full_name', person.get_full_name) for person in AppStaffProfile.objects.all()],
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        ],
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        ]
    )

    date_of_join = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=MAX_LEN_PHONE_NUMBER,
        validators=[validators.MinLengthValidator(MIN_LEN_PHONE_NUMBER), ],
        null=False,
        blank=False,
    )

    gender = models.CharField(
        max_length=MAX_LEN_GENDER,
        choices=GENDER_CHOICES,
    )

    hair_type = models.CharField(
        max_length=MAX_LEN_HAIR_TYPES,
        choices=HAIR_TYPES_CHOICES,
    )

    hair_long = models.CharField(
        max_length=MAX_LEN_HAIR_LONG,
        choices=HAIR_LONG_CHOICES,
    )

    further_explanation = models.TextField(
        max_length=MAX_LEN_FURTHER_EXPLANATION,
        null=True,
        blank=True,
    )

    is_staff = models.BooleanField(default=False, )
    is_superuser = models.BooleanField(default=False, )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name_and_phone_number(self):
        return f'{self.get_full_name} - {self.phone_number}'

    def __str__(self):
        return f'{self.get_full_name} - {self.pk}'

    class Meta:
        verbose_name = 'Customer'
