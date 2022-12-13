from django.db import models

from beauty_salon_manage_sistem.accounts.models import AppBaseUser, AppCustomerUser


class BookingCustomerProcedure(models.Model):
    MAX_PROCEDURE_LEN = 150

    hair_stylist = models.ForeignKey(AppBaseUser, on_delete=models.PROTECT)

    customer = models.ForeignKey(AppCustomerUser, on_delete=models.PROTECT)

    select_date = models.DateField(null=False, blank=False,)

    select_time = models.CharField(max_length=30,default='8:00',)

    duration_in_hours = models.FloatField(
        default=0,
        null=False,
        blank=False,)

    procedure_type = models.CharField(
        max_length=MAX_PROCEDURE_LEN,
        null=True,
        blank=True,)

    def __str__(self):
        return f'Date: {self.select_date} - {self.select_time}; Procedure: {self.procedure_type}; Client: {self.customer}; Hair stylist: {self.hair_stylist}'

    class Meta:
        ordering=['-select_date']
