from django.contrib.auth.models import AbstractUser, UserManager
from django.core import validators
from django.db import models

from beauty_salon_manage_sistem.core.validators import validate_only_letters


class AppBaseUser(AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 40

    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 40

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

    email = models.EmailField(
        unique=True,
        # null=False,
        # blank=False,
    )


class AppCustomerUser(AppBaseUser):
    MAX_LEN_PHONE_NUMBER = len('+359-888-88-88-88')
    MIN_LEN_PHONE_NUMBER = len('+359888888888')

    # TODO Make it with enumerate!
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show'),]
    MAX_LEN_GENDER = len('Do not show')

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

    phone_number = models.CharField(
        max_length=MAX_LEN_PHONE_NUMBER,
        validators=[validators.MinLengthValidator(MIN_LEN_PHONE_NUMBER),],
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

    is_staff = False
    is_superuser = False

    def __str__(self):
        return f'{self.get_full_name()} - {self.pk}'

    class Meta:
        verbose_name = 'Customer'


class AppStaffUser(AppBaseUser):
    is_staff = True
    is_superuser = False

    MAX_LEN_POSITION = 100

    position = models.CharField(
        max_length=MAX_LEN_POSITION,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.get_full_name()} - {self.position}'

    class Meta:
        verbose_name = 'Staff'

