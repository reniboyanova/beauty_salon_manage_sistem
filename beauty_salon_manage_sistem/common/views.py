from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from beauty_salon_manage_sistem.accounts.models import AppCustomerUser


# class IndexPageView(TemplateView):
#     template_name = 'common/index_page.html'


class IndexPageWithProfile(TemplateView):
    template_name = 'common/home_page_with_profile.html'


class InfoPage(TemplateView):
    template_name = 'common/info_page.html'


def index_function_view(request):
    if request.user.is_authenticated:
        return redirect('index page with profile')

    return render(request, 'common/home_page_without_log_in.html')


def search_customers(request):
    if request.method == 'POST':
        search = request.POST['search']
        searched_customers = AppCustomerUser.objects.filter(first_name__contains=search)
        context = {'search': search, 'searched_customers': searched_customers}
        return render(request, 'common/search_customers.html', context=context)
    else:
        return render(request, 'common/search_customers.html', {})
