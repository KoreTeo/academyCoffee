from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from academyCoffee.models import User, Order, UserCard, EmailSubscribe, OfferForCooperation


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
    email = forms.CharField(widget=forms.EmailInput(attrs={
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
        fields = ('first_name', 'email', 'password1', 'password2', 'region', 'PNumber', 'DateOfBirth')


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


class OrderForm(forms.ModelForm):
    addresses = [
        ('Мира, 96', 'Мира, 96'),
        ('Батурина, 13', 'Батурина, 13'),
        ('9 Мая, 22', '9 Мая, 22'),
    ]
    address = forms.CharField(widget=forms.Select(attrs={
        'id': 'regions',
        'class': 'address-select',
        'placeholder': 'Выберите город',
    }, choices=addresses))
    promocode_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'promo-code-input'
    }), required=False)

    class Meta:
        model = Order
        fields = ('address', 'serving', 'promocode_name')
        servings = [
            ('В ресторане', 'В ресторане'),
            ('С собой', 'С собой'),
        ]
        BCard = UserCard.base_card
        methods = [
            (BCard, BCard),
            ('СБП', 'СБП'),
            ('Наличными', 'Наличными'),
        ]
        widgets = {
            'serving': forms.RadioSelect(attrs={'name': 'where-to-eat'}, choices=servings),
            'payment_method': forms.RadioSelect(attrs={'name': 'where-to-eat'}, choices=methods)
        }


class CreateUserCardForm(forms.ModelForm):
    number = forms.DecimalField(widget=forms.TextInput(attrs={
        'placeholder': 'Номер карты',
    }))
    month = forms.DecimalField(widget=forms.TextInput(attrs={
        'placeholder': 'ММ',
    }))
    year = forms.DecimalField(widget=forms.TextInput(attrs={
        'placeholder': 'ГГ',
    }))
    CVCCode = forms.DecimalField(widget=forms.TextInput(attrs={
        'placeholder': 'CVC',
    }))

    class Meta:
        model = UserCard
        fields = ('number', 'month', 'year', 'CVCCode')


class SubscribeForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'email-subscribe-form',
        'placeholder': 'name@mail.ru'
    }))

    class Meta:
        model = EmailSubscribe
        fields = ('email',)


class OfferForCooperationForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'promo-code-input'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'promo-code-input'
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'promo-code-input'
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'promo-code-input'
    }))

    class Meta:
        model = OfferForCooperation
        regions = [
            ('Красноярск', 'Красноярск'),
            ('Москва', 'Москва'),
            ('Санкт-Петербург', 'Санкт-Петербург'),
            ('Новосибирск', 'Новосибирск'),
        ]
        widgets = {
            'region': forms.RadioSelect(attrs={'name': 'city'}, choices=regions),
        }
        fields = ('email', 'region', 'subject', 'name', 'text')
