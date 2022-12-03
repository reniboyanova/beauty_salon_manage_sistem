from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from beauty_salon_manage_sistem.accounts.models import AppCustomerUser
from beauty_salon_manage_sistem.procedures.forms import AddProcedureToCustomerForm
from beauty_salon_manage_sistem.procedures.models import Procedure


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


class ShowAllCustomersProcedure(ListView):
    template_name = 'procedures/show_all_customer_procedures.html'
    queryset = Procedure.objects.all()
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        customer_procedures = self.queryset.filter(customer__hair_stylist__user=self.request.user)
        context['customer_procedures'] = customer_procedures
        return context


class ProceduresDetailsView(ListView):
    template_name = 'procedures/all_beauty_salon_procedures.html'
    model = Procedure





