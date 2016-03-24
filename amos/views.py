# django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic


class IndexView(generic.base.TemplateView):
    template_name = 'index.html'
    # login_url = reverse_lazy('login')
