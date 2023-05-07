from django import forms
from .models import User, UserProfile
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'address']


# class SetPasswordForm(SetPasswordForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['new_password1', 'new_password2']
#
#
# class PasswordResetForm(PasswordResetForm):
#     def __init__(self, *args, **kwargs):
#         super(PasswordResetForm, self).__init__(*args, **kwargs)
#
#     captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())