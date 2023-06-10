from .models import Product
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, Textarea
from academyCoffee.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Телефон или почта',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    regions = [
        ('Красноярск', 'Красноярск'),
        ('Москва', 'Москва'),
        ('Санкт-Петербург', 'Санкт-Петербург'),
        ('Новосибирск', 'Новосибирск'),
    ]
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите фамилию',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите адрес эл. почты',
    }))
    region = forms.CharField(widget=forms.Select(attrs={
        'id': 'regions',
        'class': 'form-control form-control-lg  select',
        'placeholder': 'Выберите город'
    }, choices=regions))
    PNumber = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите номер телефона'
    }))
    DateOfBirth = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control datetimepicker-input',
        'data-target': '#datetimepicker1',
        'placeholder': 'Выберите дату рождения'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Подтвердите пароль'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2', 'region', 'PNumber', 'DateOfBirth')


class UserProfileForm(UserChangeForm):
    regions = [
        ('Красноярск', 'Красноярск'),
        ('Москва', 'Москва'),
        ('Санкт-Петербург', 'Санкт-Петербург'),
        ('Новосибирск', 'Новосибирск'),
    ]
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'change-name-form',
    }))
    region = forms.CharField(required=False, widget=forms.Select(attrs={
        'id': 'regions',
        'class': 'change-region-select',
        'placeholder': 'Выберите город',
    }, choices=regions))
    PNumber = forms.CharField(required=False, widget=forms.NumberInput(attrs={
        'class': 'change-number-form',
    }))
    DateOfBirth = forms.DateField(required=False, widget=forms.DateInput(attrs={
        'class': 'change-date-form datetimepicker-input',
        'data-target': '#datetimepicker1',
    }))

    class Meta:
        model = User
        fields = ('first_name', 'region', 'PNumber', 'DateOfBirth')
