# Generated by Django 4.1.3 on 2022-12-07 11:17

import beauty_salon_manage_sistem.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_type_of_procedure', multiselectfield.db.fields.MultiSelectField(choices=[('Cut', 'Cut'), ('Color', 'Color'), ('Blow', 'Blow'), ('Styling', 'Styling'), ('Treatments', 'Treatments')], max_length=1000)),
                ('washing_hair', models.BooleanField(blank=True, default='Yes')),
                ('color_type_of_procedure', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Overall Color', 'Overall Color'), ('Frame Foil', 'Frame Foil'), ('Full Foil', 'Full Foil'), ('Partial Foil', 'Partial Foil'), ('Balayage', 'Balayage'), ('Root Smudge', 'Root Smudge'), ('Gloss', 'Gloss')], max_length=30, null=True)),
                ('product_used_for_color', models.TextField(blank=True, null=True)),
                ('cut_type_of_procedure', models.CharField(blank=True, choices=[("Women's haircut", "Women's haircut"), ("Men's haircut", "Men's haircut"), ("Child's haircut", "Child's haircut")], max_length=16, null=True)),
                ('comment_about_haircut', models.TextField(blank=True, null=True)),
                ('styling_type_of_procedure', models.CharField(blank=True, choices=[('Bridal hairstyle', 'Bridal hairstyle'), ('Formal hairstyle', 'Formal hairstyle'), ('Hair curling', 'Hair curling'), ('Bun curling', 'Bun curling')], max_length=17, null=True)),
                ('comment_about_styling', models.TextField(blank=True, null=True)),
                ('treatment_type_of_procedure', models.CharField(blank=True, choices=[('KERATIN therapy', 'KERATIN therapy'), ('ARGAN therapy', 'ARGAN therapy'), ('PROTEIN therapy', 'PROTEIN therapy')], max_length=16, null=True)),
                ('product_used_for_treatment', models.TextField(blank=True, null=True)),
                ('other_comments', models.TextField(blank=True, null=True)),
                ('before_image', models.ImageField(upload_to='before images', validators=[beauty_salon_manage_sistem.core.validators.validate_image_size])),
                ('after_image', models.ImageField(upload_to='after images', validators=[beauty_salon_manage_sistem.core.validators.validate_image_size])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.appcustomeruser')),
            ],
        ),
    ]
