from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import forms, models, middlewares


class RegistrationView(CreateView):
    form_class = forms.CustomRegistrationForm
    template_name = 'users/regsiter.html'  # Исправлено название шаблона
    success_url = reverse_lazy('users:login')  # Используем именованный URL


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'


    def get_success_url(self):
        return reverse("users:user_list")


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = models.CustomUser
    context_object_name = 'person'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
