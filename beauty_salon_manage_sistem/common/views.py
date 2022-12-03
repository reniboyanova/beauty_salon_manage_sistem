from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'common/index_page.html'


class IndexPageWithProfile(TemplateView):
    template_name = 'common/home_page_with_profile.html'
