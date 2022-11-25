from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from beauty_salon_manage_sistem.procedures.forms import AddProcedureToCustomerForm


class AddProcedureToCustomer(CreateView):
    template_name = 'procedures/adding_procedure_to_customer.html'
    form_class = AddProcedureToCustomerForm
    success_url = reverse_lazy('add procedure to customer')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                f.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)