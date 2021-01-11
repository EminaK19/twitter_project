from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import User


# class RegisterForm(forms.ModelForm):
#     password   = forms.CharField(widget=forms.PasswordInput)
#     password2  = forms.CharField(label='Confirm password', widget=forms.PasswordInput)


#     class Meta:
#         model = User
#         fields = ['username', 'email',]


#     def cleaned_data(self):
#         username = self.cleaned_data.get('username')
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email=email)
#         if qs:
#             raise forms.ValidationError('given email is taken')
#         return email 

#     def cleaned_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Password don't match!")
#         return password2


class UserRegistrationForm(UserCreationForm):
    """Form for register user"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')
        user = get_user_model().object.create_user(username=username, email=email, password=password)
        #MyUser.object.create_user
        return user


# class UserAdminCreationForm(forms.ModelForm):
#     """
#     A form for creating new users. Includes all the required
#     fields, plus a repeated password.
#     """

#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)


#     class Meta:
#         model = User
#         fields = ['email', ]


#     def cleaned_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Password don't match!")
#         return password2

#     def save(self, commit=True):
#     # Save the provided password in hashed format

#         user = super(UserAdminCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data['password1'])
#         if commit:
#             user.save()
#         return user

# class UserAdminChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
    # """

    # password = ReadOnlyPasswordHashField()

    # class Meta:
    #     model = User
    #     fields = ['email', 'password', 'is_active', 'is_superuser']


    # def clean_password(self):
    #     # Regardless of what the user provides, return the initial value.
    #     # This is done here, rather than on the field, because the
    #     # field does not have access to the initial value
    #     return self.initial["password"]


