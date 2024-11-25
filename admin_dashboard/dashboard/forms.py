from django import forms
from .models import User, Role

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'role', 'status']
        widgets = {
            'status': forms.CheckboxInput(),
        }

from django import forms
from .models import Role

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'permissions']  # Include fields from your Role model


