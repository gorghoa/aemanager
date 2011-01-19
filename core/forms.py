from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput
from django.utils.translation import ugettext_lazy as _

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class PasswordForm(forms.Form):
    current_password = forms.CharField(label=_('Current password'), widget=PasswordInput(render_value=False))
    new_password = forms.CharField(label=_('New password'), widget=PasswordInput(render_value=False))
    retyped_new_password = forms.CharField(label=_('Retype password'), widget=PasswordInput(render_value=False))

    def clean(self):
        cleaned_data = self.cleaned_data
        new_password = cleaned_data.get("new_password")
        retyped_new_password = cleaned_data.get("retyped_new_password")

        if new_password <> retyped_new_password:
            self._errors["retyped_new_password"] = self.error_class([_("Password doesn't match")])
            del cleaned_data['retyped_new_password']

        return cleaned_data
