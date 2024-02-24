from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from .models import Profile
# this is intended to provide a form according to request

class UserRegisterForm(UserCreationForm):
    """
    Registering a user
    """
    email = forms.EmailField()

    class Meta:
        # This class allows you to specify metadata for the model
        # for this case it specifies our model to refer to its User
        # then the fields to be specified in our form
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    """
    Updating username and email
    """
    email = forms.EmailField()

    class Meta:
        # metadata for this class include
        # model to be refered to is User
        # fields to be used are username and email only
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    profile update form
    """
    class Meta:
        # metadata to be used are
        #  Profile model which is connected to the user model
        # then the image field
        model = Profile
        fields = ['image']