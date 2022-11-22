from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from beauty_salon_manage_sistem.accounts.forms import RegistrationAppUserForm, AddingCustomerForm
from beauty_salon_manage_sistem.accounts.models import AppCustomerUser, AppStaffProfile

UserModel = get_user_model()


class ShowAppUsers(ListView):
    model = UserModel
    template_name = 'accounts/show_app_users.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['staffs'] = UserModel.objects.all()
        context['customers'] = AppCustomerUser.objects.all()
        return context


class CreateAppStaffUser(CreateView):
    template_name = 'accounts/staff_creation_form.html'
    form_class = RegistrationAppUserForm
    success_url = reverse_lazy('index page')

    def form_valid(self, form):
        result = super().form_valid(form)
        # user => self.object
        # request => self.request
        login(self.request, self.object)
        return result


class CreateCustomer(CreateView):
    template_name = 'accounts/adding_customer.html'
    form_class = AddingCustomerForm
    success_url = reverse_lazy('add customer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['hairstylists'] = [person.get_full_name for person in AppStaffProfile.objects.all()]
        return context
