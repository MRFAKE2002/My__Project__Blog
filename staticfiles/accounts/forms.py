from django.contrib.auth.forms import UserCreationForm , UserChangeForm


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        fields = ['username', 'email']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        fields = ['username', 'email']
        
