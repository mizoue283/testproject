from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .forms import RegisterForm, LoginForm


class TopPageView(generic.TemplateView):
    template_name = "testapp/index.html"


class MyPageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "testapp/info.html"


class CreateUserView(generic.CreateView):
    template_name = 'testapp/create.html'
    form_class = RegisterForm
    success_url = reverse_lazy('testapp:index')


def login(request):
    context = {
        'template_name': 'testapp/login.html',
        'authentication_form': LoginForm
    }
    return auth_views.login(request, **context)


def logout(request):
    context = {
        'template_name': 'testapp/index.html',
    }
    return auth_views.logout(request, **context)
