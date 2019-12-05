from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', )

class UpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', )