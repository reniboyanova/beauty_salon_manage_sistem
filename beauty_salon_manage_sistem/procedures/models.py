from multiselectfield import MultiSelectField
from django.db import models
from cloudinary.models import CloudinaryField


from beauty_salon_manage_sistem.accounts.models import AppCustomerUser
from beauty_salon_manage_sistem.core.validators import validate_image_size

class Procedure(models.Model):
    MAX_LEN_CHOICES = 1000

    MAX_CHOICES = 4

    MAX_LEN_COLOR_TYPE_OF_PROCEDURE = 30

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
        max_length=MAX_LEN_CHOICES,
        max_choices=MAX_CHOICES,
        null=False,
        blank=False,
        verbose_name='Main type of procedure:'
    )

    washing_hair = models.BooleanField(
        null=False,
        blank=True,
        verbose_name='Is hair washing included? (Yes/No):'
    )

    color_type_of_procedure = MultiSelectField(
        choices=COLOR_TYPE_OF_PROCEDURE_CHOICES,
        null=True,
        blank=True,
        max_length=MAX_LEN_COLOR_TYPE_OF_PROCEDURE,
        verbose_name='Type of hair coloring:'
    )

    product_used_for_color = models.TextField(
        null=True,
        blank=True,
        verbose_name='Products used for coloring:'
    )

    cut_type_of_procedure = models.CharField(
        max_length=MAX_LEN_CUT_TYPE_PROCEDURE,
        choices=CUT_TYPE_OF_PROCEDURE_CHOICES,
        null=True,
        blank=True,
        verbose_name='Haircut type:'
    )

    comment_about_haircut = models.TextField(
        null=True,
        blank=True,
        verbose_name='Comment about haircut:'
    )

    styling_type_of_procedure = models.CharField(
        max_length=MAX_LEN_STYLING_TYPE_PROCEDURE,
        choices=STYLING_TYPE_OF_PROCEDURE_CHOICES,
        null=True,
        blank=True,
        verbose_name='Hair styling services:'
    )

    comment_about_styling = models.TextField(
        null=True,
        blank=True,
        verbose_name='Comment about hair styling:'
    )

    treatment_type_of_procedure = models.CharField(
        max_length=MAX_LEN_TREATMENT_TYPE_PROCEDURE,
        choices=TREATMENT_TYPE_OF_PROCEDURE_CHOICES,
        null=True,
        blank=True,
        verbose_name='Treatment procedure:'
    )

    product_used_for_treatment = models.TextField(
        null=True,
        blank=True,
        verbose_name='Products used for treatment:'
    )

    other_comments = models.TextField(
        null=True,
        blank=True,
        verbose_name='Other comments:'
    )

    customer = models.ForeignKey(
        AppCustomerUser,
        on_delete=models.CASCADE,
    )

    # before_image = models.ImageField(upload_to='before images', validators=[validate_image_size,])
    # after_image = models.ImageField(upload_to='after images', validators=[validate_image_size,])
    before_image = CloudinaryField('before images', validators=[validate_image_size,])
    after_image = CloudinaryField('after images', validators=[validate_image_size,])

    date = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return f'{self.main_type_of_procedure} - {self.customer.get_full_name} on {self.date}'






