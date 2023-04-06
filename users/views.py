from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from products.models import Basket
from .forms import UserRegistrationForm, UserProfileForm, UserLoginForm
from .models import User, EmailVerification


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегестрировались'


class UserProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


class EmailVerificationView(TemplateView):
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)

        if email_verifications.exists():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
