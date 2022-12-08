from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView


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

