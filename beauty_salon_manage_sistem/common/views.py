from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

from beauty_salon_manage_sistem.accounts.models import AppCustomerUser
from beauty_salon_manage_sistem.common.forms import BookingForm, BookingFormDeleteForm
from beauty_salon_manage_sistem.common.models import BookingCustomerProcedure


class IndexPageWithProfile(LoginRequiredMixin, TemplateView):
    template_name = 'common/home_page_with_profile.html'


class InfoPage(TemplateView):
    template_name = 'common/info_page.html'


def index_function_view(request):
    if request.user.is_authenticated:
        return redirect('index page with profile')

    return render(request, 'common/home_page_without_log_in.html')


@login_required
def search_customers(request):
    if request.method == 'POST':
        search = request.POST['search']
        searched_customers = AppCustomerUser.objects.filter(first_name__contains=search)
        context = {'search': search, 'searched_customers': searched_customers}
        return render(request, 'common/search_customers.html', context=context)
    else:
        return render(request, 'common/search_customers.html', {})


def handle_not_found(request, exception):
    return render(request, '404.html')


class BookingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'common/booking_procedure/booking_customer_procedure.html'
    form_class = BookingForm
    success_url = reverse_lazy('index page with profile')


class BookingListView(LoginRequiredMixin, ListView):
    template_name = 'common/booking_procedure/list_booking_customer.html'
    queryset = BookingCustomerProcedure.objects.all()
    success_url = reverse_lazy('index page with profile')
    paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        my_booking_procedure = self.queryset.filter(hair_stylist=self.request.user)
        context['my_booking_procedure'] = my_booking_procedure
        return context

class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = BookingCustomerProcedure
    success_url = reverse_lazy('my booking hours')
    form_class = BookingFormDeleteForm
    template_name = 'common/booking_procedure/delete_booking_procedure.html'


