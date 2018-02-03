from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import password_validation, get_user_model


User = get_user_model()


class TequioUserCreationForm(UserCreationForm):
    """
    Based in part on
    http://django-authtools.readthedocs.io/en/latest/how-to/invitation-email.
    A UserCreationForm with optional password inputs.
    """
    class Meta:
        """
        Identical to Meta from Django's UserCreationForm,
        except using custom User model
        """
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super(TequioUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        # if password1 and password2 and password1 != password2:
        if password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        # only validate password if it has been provided
        if password2:
            self.instance.username = self.cleaned_data.get('username')
            password_validation.validate_password(
                self.cleaned_data.get('password2'), self.instance)
        return password2
