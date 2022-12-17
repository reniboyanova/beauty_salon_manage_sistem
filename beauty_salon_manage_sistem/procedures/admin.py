from django.contrib import admin

from beauty_salon_manage_sistem.procedures.forms import AddProcedureToCustomerForm
from beauty_salon_manage_sistem.procedures.models import Procedure


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    add_form = AddProcedureToCustomerForm
    ordering = ['-date',]
