from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django import forms as frm

from django.contrib.auth.forms import UserChangeForm, AdminUserCreationForm
from .models import CustomUser


class CustomUserCreationForm(AdminUserCreationForm):
    usable_password = None

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'last_name', 'first_name', 'father_name', 'phone_number', 'personal_code',
                  'age', 'father_phone_number']
        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل',
            'last_name': 'نام',
            'first_name': 'نام خانوادگی',
            'father_name': 'نام پدر',
            'phone_number': 'شماره تماس',
            'personal_code': 'کدملی',
            'age': 'سن',
            'father_phone_number': 'شماره تماس پدر',

        }

        help_texts = {
            'username': 'فقظ حروف انگلیسی و اعداد',
        }

        error_messages = {
            'username': {
                'required': 'وارد کردن نام کاربری الزامی است',
                'unique': 'این نام کاربری قبلا انتخاب شده است',
                'invalid': 'نام کاربری معتبر نیست',
            },
            'سن': {
                'required': 'وارد کردن تاریخ تولد الزامی است.',
                'invalid': 'تاریخ تولد وارد شده معتبر نیست',
            }

        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
