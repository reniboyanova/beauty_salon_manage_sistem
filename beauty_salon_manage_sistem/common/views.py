from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'common/index_page.html'
