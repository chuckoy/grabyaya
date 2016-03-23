# django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView


class IndexView(LoginRequiredMixin, ListView):
    template_url = 'index.html'
    login_url = reverse_lazy('login')
