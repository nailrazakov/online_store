from django.forms import BooleanField
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class UserForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']
