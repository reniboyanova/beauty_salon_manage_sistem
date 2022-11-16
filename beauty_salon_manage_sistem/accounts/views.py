from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from beauty_salon_manage_sistem.accounts.forms import CreateAppCustomerUserForm, CreateAppStaffUserForm
from beauty_salon_manage_sistem.accounts.models import AppCustomerUser, AppStaffUser

UserModel = get_user_model()


class ShowAppUsers(ListView):
    model = UserModel
    template_name = 'accounts/show_app_users.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['customers'] = AppCustomerUser.objects.all()
        context['staffs'] = AppStaffUser.objects.all()
        return context


class CreateAppCustomerUser(CreateView):
    template_name = 'accounts/customer_profile_creation.html'
    form_class = CreateAppCustomerUserForm
    success_url = reverse_lazy('index page')


class CreateAppStaffUser(CreateView):
    template_name = 'accounts/staff_creation_form.html'
    form_class = CreateAppStaffUserForm
    success_url = reverse_lazy('index page')

