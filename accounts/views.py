from django.contrib.auth.views import LoginView
from django.views import generic
from django import forms as frm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

from .models import CustomUser


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'Registrtions/signup.html'
    model = CustomUser
    success_url = reverse_lazy('loginPage')


    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password1'].label = 'رمز عبور'
        form.fields['password1'].widget = frm.PasswordInput(attrs={'placeholder': 'رمز عبور'})
        form.fields['password1'].help_text = 'رمز عبور حداقل 8 رقم'
        form.fields['password1'].required = True

        form.fields['password2'].label = 'تکرار رمز عبور'
        form.fields['password2'].widget = frm.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'})
        form.fields['password2'].help_text = 'رمز عبور وارد شده را تکرار کنید.'
        form.fields['password2'].required = True

        form.fields['email'].required = True

        return form


    def form_valid(self, form):
        return super().form_valid(form)


class LoginPageView(LoginView):

    template_name = 'Registrtions/login.html'
    model = CustomUser
    success_url = reverse_lazy('all_courses')



