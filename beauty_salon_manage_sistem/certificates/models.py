from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ProfessionalCertificate(models.Model):
    MAX_LEN_COURSE = 150

    MAX_LEN_ORGANIZATION_NAME = 150

    MAX_LEN_QUALIFICATION = 150

    MAX_LEN_SERIAL_NUMBER = 30

    course_name = models.CharField(
        max_length=MAX_LEN_COURSE,
        verbose_name='Professional course name:',
        null=False,
        blank=False,
    )

    organization_name = models.CharField(
        max_length=MAX_LEN_ORGANIZATION_NAME,
        null=False,
        blank=False,
        verbose_name='Product type:',
    )

    qualification = models.CharField(
        max_length=MAX_LEN_QUALIFICATION,
        null=False,
        blank=False,
        verbose_name='Qualification type:'
    )

    serial_number = models.CharField(
        max_length=MAX_LEN_SERIAL_NUMBER,
        null=True,
        blank=True,
        verbose_name='Serial number:',
    )

    image_of_certificate = models.URLField(
        verbose_name='Certificate image:',
    )

    date_of_certificate = models.DateField(
        verbose_name='Certificate date:',
    )

    valid_until = models.DateField(
        verbose_name='Valid until:',
    )

    certificate_owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def information_about_certificate(self):
        return f'{self.course_name} from {self.organization_name} valid until {self.valid_until}'

    def __str__(self):
        return f'{self.course_name}, owned by {self.certificate_owner}'

    class Meta:
        verbose_name_plural = 'Professional certificates'
        ordering = ['-date_of_certificate']
