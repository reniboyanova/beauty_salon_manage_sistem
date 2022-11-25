from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from beauty_salon_manage_sistem.accounts.forms import RegistrationAppUserForm, AddingCustomerForm
from beauty_salon_manage_sistem.accounts.models import AppCustomerUser, AppStaffProfile

UserModel = get_user_model()


class ShowAppUsers(ListView):
    model = UserModel
    template_name = 'accounts/show_app_customrs.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['staffs'] = UserModel.objects.all()
        context['customers'] = AppCustomerUser.objects.all()
        context['my_customers'] = AppCustomerUser.objects.filter(hair_stylist__user=self.request.user)

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


class SignInView(LoginView):
    template_name = 'accounts/login_page.html'


class SignOutView(LogoutView):
    next_page = reverse_lazy('index page')


class AppProfileUpdateView(UpdateView):
    model = AppStaffProfile
    fields = ('first_name', 'last_name', 'position')
    template_name = 'accounts/edit_app_user_profile.html'

    def get_success_url(self):
        return reverse_lazy('index page')


class AppProfileDetailsView(DetailView):
    template_name = 'accounts/details_app_user_profile.html'
    model = AppStaffProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['customers_count'] = self.object.appcustomeruser_set.count()
        context['customers'] = self.object.appcustomeruser_set.all()
        # photos = self.object.photo_set.all(). \
        #     prefetch_related('like_set')
        #
        # context['photos_count'] = photos.count()
        # context['photo_likes'] = sum(x.like_set.count() for x in photos)

        return context

