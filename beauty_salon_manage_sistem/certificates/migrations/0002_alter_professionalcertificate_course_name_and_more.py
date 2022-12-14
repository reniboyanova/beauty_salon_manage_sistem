# Generated by Django 4.1.3 on 2022-12-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalcertificate',
            name='course_name',
            field=models.CharField(max_length=150, verbose_name='Professional course name:'),
        ),
        migrations.AlterField(
            model_name='professionalcertificate',
            name='date_of_certificate',
            field=models.DateField(verbose_name='Certificate date:'),
        ),
        migrations.AlterField(
            model_name='professionalcertificate',
            name='image_of_certificate',
            field=models.URLField(verbose_name='Certificate image:'),
        ),
        migrations.AlterField(
            model_name='professionalcertificate',
            name='organization_name',
            field=models.CharField(max_length=150, verbose_name='Product type:'),
        ),
        migrations.AlterField(
            model_name='professionalcertificate',
            name='qualification',
            field=models.CharField(max_length=150, verbose_name='Qualification type:'),
        ),
        migrations.AlterField(
            model_name='professionalcertificate',
            name='serial_number',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Serial number:'),
        ),
        migrations.AlterField(
            model_name='professionalcertificate',
            name='valid_until',
            field=models.DateField(verbose_name='Valid until:'),
        ),
    ]
