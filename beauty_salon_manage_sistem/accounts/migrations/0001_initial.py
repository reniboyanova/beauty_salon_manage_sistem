# Generated by Django 4.1.3 on 2022-11-15 10:11

import beauty_salon_manage_sistem.core.validators
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppBaseUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(2), beauty_salon_manage_sistem.core.validators.validate_only_letters])),
                ('last_name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(2), beauty_salon_manage_sistem.core.validators.validate_only_letters])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AppCustomerUser',
            fields=[
                ('appbaseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.MinLengthValidator(13)])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], max_length=11)),
                ('hair_type', models.CharField(choices=[('Straight hair', 'Straight hair'), ('Wavy hair', 'Wavy hair'), ('Curly hair', 'Curly hair'), ('Kinky hair', 'Kinky hair'), ('I am not sure', 'I am not sure')], max_length=13)),
                ('hair_long', models.CharField(choices=[('Short hair', 'Short hair'), ('Middle hair', 'Middle hair'), ('Long hair', 'Long hair'), ('Very long hair', 'Very long hair'), ('I am not sure', 'I am not sure')], max_length=14)),
                ('further_explanation', models.TextField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Customer',
            },
            bases=('accounts.appbaseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AppStaffUser',
            fields=[
                ('appbaseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('position', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Staff',
            },
            bases=('accounts.appbaseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]