from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # make sure email is required

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=150 ,required=True)
