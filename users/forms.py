from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User

        fields = '__all__'


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'telephone':
                field.widget.attrs['class'] = 'mask-phone form-control'
                

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',
                  'email', 'position', 'telephone', 'avatar', 'market_number')

        widgets = {
            'telephone': forms.widgets.TextInput(attrs={'type': 'tel', }),
        }


class UserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'telephone':
                field.widget.attrs['class'] = 'mask-phone form-control'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'avatar', 'telephone', 'market_number')
