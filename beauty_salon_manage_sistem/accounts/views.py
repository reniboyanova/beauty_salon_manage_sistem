from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from beauty_salon_manage_sistem.accounts.forms import RegistrationAppUserForm, AddingCustomerForm, AppProfileDeleteForm
from beauty_salon_manage_sistem.accounts.models import AppCustomerUser, AppStaffProfile

UserModel = get_user_model()


class ShowAppCustomers(LoginRequiredMixin, ListView):
    model = AppCustomerUser
    template_name = 'accounts/customers_accounts/show_app_customrs.html'
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['staffs'] = UserModel.objects.all()
        context['customers'] = AppCustomerUser.objects.all()
        context['my_customers'] = AppCustomerUser.objects.filter(hair_stylist__user=self.request.user)
        context['my_booking_hours'] = UserModel.objects.filter()

        return context


class CreateAppStaffUser(CreateView):
    template_name = 'accounts/users_accounts/staff_creation_form.html'
    form_class = RegistrationAppUserForm
    success_url = reverse_lazy('index page with profile')

    def form_valid(self, form):
        result = super().form_valid(form)
        # user => self.object
        # request => self.request
        login(self.request, self.object)
        return result


class CreateAppStaffUserFromManager(CreateView):
    template_name = 'accounts/users_accounts/staff_creation_from_manager.html'
    form_class = RegistrationAppUserForm
    success_url = reverse_lazy('add staff')


class CreateCustomer(LoginRequiredMixin, CreateView):
    template_name = 'accounts/customers_accounts/adding_customer.html'
    form_class = AddingCustomerForm
    success_url = reverse_lazy('add customer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['hairstylists'] = [person.get_full_name for person in AppStaffProfile.objects.all()]
        return context


class SignInView(LoginView):
    template_name = 'accounts/login_page.html'


class SignOutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('index page')


class AppStaffProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = AppStaffProfile
    fields = ('first_name', 'last_name', 'position')
    template_name = 'accounts/users_accounts/edit_app_user_profile.html'

    def get_success_url(self):
        return reverse_lazy('index page with profile')


class AppStaffProfileDetailsView(DetailView):
    template_name = 'accounts/users_accounts/details_app_user_profile.html'
    model = AppStaffProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['customers_count'] = self.object.appcustomeruser_set.count()
        context['customers'] = self.object.appcustomeruser_set.all()

        return context


class SuperUserProfileDetailsView(LoginRequiredMixin, ListView):
    template_name = 'accounts/users_accounts/details_app_user_profile_for_superuser.html'
    model = UserModel
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['staffs'] = AppStaffProfile.objects.all()
        return context


class AppCustomerProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = AppCustomerUser
    form_class = AppProfileDeleteForm
    success_url = reverse_lazy('index page with profile')

    template_name = "accounts/customers_accounts/delete_appcustomer_profile.html"


class AppCustomerProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = AppCustomerUser
    fields = ('hair_stylist', 'last_name', 'phone_number', 'hair_long', 'hair_type',)
    template_name = 'accounts/customers_accounts/edit_appcustomer_profile.html'

    def get_success_url(self):
        return reverse_lazy('index page with profile')


class ShowCurrentCustomerProcedure(DetailView):
    template_name = 'procedures/show_current_customer_procedure.html'
    model = AppCustomerUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_customers_has_procedures'] = self.object.procedure_set.all()

        return context
