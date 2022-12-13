# Generated by Django 4.1.3 on 2022-12-10 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=150, verbose_name='Professional course name')),
                ('organization_name', models.CharField(max_length=150, verbose_name='Product type')),
                ('qualification', models.CharField(max_length=150, verbose_name='Qualification type')),
                ('serial_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Serial number')),
                ('image_of_certificate', models.URLField(verbose_name='Certificate image')),
                ('date_of_certificate', models.DateField(verbose_name='Certificate date')),
                ('valid_until', models.DateField(verbose_name='Valid until')),
                ('certificate_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Professional certificates',
                'ordering': ['-date_of_certificate'],
            },
        ),
    ]