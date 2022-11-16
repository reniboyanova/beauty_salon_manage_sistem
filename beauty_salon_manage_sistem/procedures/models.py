from multiselectfield import MultiSelectField
from django.db import models

from beauty_salon_manage_sistem.accounts.models import AppCustomerUser


# TODO да изнеса различните CHOICES в отделен файл с клас и пропъртита

# TODO да оправя хардкоднатите стойности

# TODO да сложа снимки "Преди" и "След"


class Procedure(models.Model):
    MAIN_TYPE_OF_PROCEDURE_CHOICES = (
        ('Cut', 'Cut'),
        ('Color', 'Color'),
        ('Blow', 'Blow'),
        ('Styling', 'Styling'),
        ('Treatments', 'Treatments'),
    )

    COLOR_TYPE_OF_PROCEDURE_CHOICES = [
        ('Overall Color', 'Overall Color'),
        ('Frame Foil', 'Frame Foil'),
        ('Full Foil', 'Full Foil'),
        ('Partial Foil', 'Partial Foil'),
        ('Balayage', 'Balayage'),
        ('Root Smudge', 'Root Smudge'),
        ('Gloss', 'Gloss'),
    ]

    CUT_TYPE_OF_PROCEDURE_CHOICES = [
        ('Women\'s haircut', 'Women\'s haircut'),
        ('Men\'s haircut', 'Men\'s haircut'),
        ('Child\'s haircut', 'Child\'s haircut'),
    ]

    MAX_LEN_CUT_TYPE_PROCEDURE = len('Women\'s haircut') + 1

    STYLING_TYPE_OF_PROCEDURE_CHOICES = [
        ('Bridal hairstyle', 'Bridal hairstyle'),
        ('Formal hairstyle', 'Formal hairstyle'),
        ('Hair curling', 'Hair curling'),
        ('Bun curling', 'Bun curling'),
    ]

    MAX_LEN_STYLING_TYPE_PROCEDURE = len('Bridal hairstyle') + 1

    TREATMENT_TYPE_OF_PROCEDURE_CHOICES = [
        ('KERATIN therapy', 'KERATIN therapy'),
        ('ARGAN therapy', 'ARGAN therapy'),
        ('PROTEIN therapy', 'PROTEIN therapy'),
    ]

    MAX_LEN_TREATMENT_TYPE_PROCEDURE = len('PROTEIN therapy') + 1

    main_type_of_procedure = MultiSelectField(
        choices=MAIN_TYPE_OF_PROCEDURE_CHOICES,
        max_length=1000,
        max_choices=4,
        null=False,
        blank=False,
    )

    washing_hair = models.BooleanField(
        default='Yes',
        null=False,
        blank=True,
    )

    color_type_of_procedure = MultiSelectField(
        choices=COLOR_TYPE_OF_PROCEDURE_CHOICES,
        null=True,
        blank=True,
        max_length=30,
    )

    product_used_for_color = models.TextField(
        null=True,
        blank=True,
    )

    cut_type_of_procedure = models.CharField(
        max_length=MAX_LEN_CUT_TYPE_PROCEDURE,
        choices=CUT_TYPE_OF_PROCEDURE_CHOICES,
        null=True,
        blank=True,
    )

    comment_about_haircut = models.TextField(
        null=True,
        blank=True,
    )

    styling_type_of_procedure = models.CharField(
        max_length=MAX_LEN_STYLING_TYPE_PROCEDURE,
        choices=STYLING_TYPE_OF_PROCEDURE_CHOICES,
        null=True,
        blank=True,
    )

    comment_about_styling = models.TextField(
        null=True,
        blank=True,
    )

    treatment_type_of_procedure = models.CharField(
        max_length=MAX_LEN_TREATMENT_TYPE_PROCEDURE,
        choices=TREATMENT_TYPE_OF_PROCEDURE_CHOICES,
        null=True,
        blank=True,
    )

    product_used_for_treatment = models.TextField(
        null=True,
        blank=True,
    )

    other_comments = models.TextField(
        null=True,
        blank=True,
    )

    customer = models.ForeignKey(
        AppCustomerUser,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.main_type_of_procedure} - {self.customer.get_full_name()}'



