from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.views.generic import DetailView, FormView, ListView, TemplateView

from .forms import LoginForm, SignUpForm
from .tokens import account_activation_token


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect(reverse_lazy('login'))


@login_required
def home(request):
    return render(request, 'account/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode("utf-8"),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'acoount/account_activation_invalid.html')


class LoginView(FormView):
    template_name = "account/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("post:post-list")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class ProfileView(TemplateView):
    template_name = 'account/profile.html'


class ProfileSettingsView(TemplateView):
    template_name = 'account/profile-settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
