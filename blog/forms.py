from django import forms
from django.contrib.auth import password_validation, authenticate
from django.core.exceptions import ValidationError
from django.forms import PasswordInput

from django.utils.translation import gettext as _

from .models import CustomUser, Article


class RegisterForm(forms.ModelForm):
    login = forms.CharField(min_length=3, max_length=30, widget=forms.TextInput(
        attrs={'class': "form-control", 'id': "register-login", 'onkeyup': "validateRegisterLogin()",
               'placeholder': "Login", "autofocus": ""}))
    password1 = forms.CharField(strip=False, min_length=6, max_length=34, widget=PasswordInput(
        attrs={'onkeyup': 'validatePassword1Register()', 'id': "register-password1", 'class': "form-control",
               'placeholder': "Heslo", "autofocus": "autofocus", }))

    email = forms.EmailField(max_length=50, widget=forms.EmailInput(
        attrs={'onkeyup': 'validateEmail()', 'id': "register-email", 'class': "form-control",
               'placeholder': "Email", "autofocus": "autofocus"}))

    password2 = forms.CharField(strip=False, min_length=6, max_length=34, widget=PasswordInput(
        attrs={'onkeyup': 'validatePassword2Register()', 'id': "register-password2", 'class': "form-control",
               'placeholder': "Zopakuj Heslo", "autofocus": "autofocus", }))

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }

    class Meta:
        model = CustomUser
        fields = ['login', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.ModelForm):
    login = forms.CharField(min_length=3, max_length=30, widget=forms.TextInput(
        attrs={'class': "form-control", 'id': "login-login", 'onkeyup': "validateLoginLogin()", 'placeholder': "Login",
               "autofocus": "autofocus"}))
    password = forms.CharField(strip=False, min_length=6, max_length=34, widget=PasswordInput(
        attrs={'onkeyup': 'validatePasswordLogin()', 'id': "login-password", 'class': "form-control",
               'placeholder': "Heslo", "autofocus": "autofocus"}))

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.auth = None
        super().__init__(*args, **kwargs)

    def clean(self):
        login = self.cleaned_data.get("login")
        password = self.cleaned_data.get("password")

        if login is not None and password:
            self.auth = authenticate(
                self.request, username=login, password=password
            )
            if self.auth is None:
                self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.auth)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

    def get_user(self):
        return self.auth

    def get_invalid_login_error(self):
        raise forms.ValidationError(
            self.error_messages['invalid_login'],
            code="invalid_login",
            params={"username": self.cleaned_data.get("login")},
        )

    class Meta:
        model = CustomUser
        fields = ['login', 'password']
