from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.core.signing import BadSignature
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
# from django.views.generic import TemplateView

from .forms import AccountRegisterForm, AccountUpdateForm
from .utils import signer


class AccountRegisterView(CreateView):
    model = get_user_model()
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:register_done')
    form_class = AccountRegisterForm


# class AccountRegisterDoneView(TemplateView):
#     template_name = 'accounts/register_done.html'


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'accounts/bad_signature.html')

    user = get_object_or_404(get_user_model(), username=username)
    if user.is_activated:
        template = 'accounts/user_is_activated.html'
    else:
        template = 'accounts/activation_done.html'
        user.is_activated = True
        user.is_active = True
        user.save()

    return render(request, template)


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url

        return reverse('index')


class AccountLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


def account_profile_view(request):
    return render(request, 'accounts/profile.html')


class AccountUpdateProfileView(UpdateView):
    template_name = 'accounts/profile_update.html'
    model = get_user_model()
    success_url = reverse_lazy('accounts:profile')
    form_class = AccountUpdateForm

    def get_object(self, queryset=None):
        return self.request.user
