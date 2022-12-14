from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','age', 'tagline', 'email')

class CustomerUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','age', 'tagline', 'email')

