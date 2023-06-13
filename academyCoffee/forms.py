from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from phonenumber_field.modelfields import PhoneNumberField

from academyCoffee.models import User


class UserLoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'
    }))

    username = PhoneNumberField(region="RU")

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control py-4',
            'placeholder': 'Введите номер телефона(+7)'
        })

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
    PNumber = PhoneNumberField(region="RU")
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

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['PNumber'].widget.attrs.update({'class': 'form-control py-4'})

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
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'change-name-form',
    }))
    region = forms.CharField(widget=forms.Select(attrs={
        'id': 'regions',
        'class': 'change-region-select',
        'placeholder': 'Выберите город',
    }, choices=regions))
    PNumber = PhoneNumberField(region='RU')
    DateOfBirth = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'change-date-form datetimepicker-input',
        'data-target': '#datetimepicker1',
    }))

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['PNumber'].widget.attrs.update({'class': 'change-number-form'})

    class Meta:
        model = User
        fields = ('first_name', 'region', 'PNumber', 'DateOfBirth')
