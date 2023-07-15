from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import Group


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label = "Имя", 
                widget=forms.TextInput(attrs={
                'type': 'text',
                'name': 'text',
                'placeholder': 'Имя',
                'class': 'form-control me-2',
                }), required=False)
    
    last_name = forms.CharField(label = "Фамилия", 
                widget=forms.TextInput(attrs={
                'cols': 60, 'rows': 10,
                'type': 'text',
                'name': 'text',
                'placeholder': 'Фамилия',
                'class': 'form-control me-2',
                }), required=False)
    
    password1 = forms.CharField(max_length=16, 
                widget=forms.PasswordInput(attrs={
                'class': 'form-control'}), label='Password')
    
    password2 = forms.CharField(max_length=16, 
                widget=forms.PasswordInput(attrs={
                'class': 'form-control'}), label='Confirm Password')
  
    class Meta:
        model = User
        fields = (
            "username",
            'first_name',
            'last_name',
            "email",
            "password1",
            "password2",
            )
        widgets = {
           'username': forms.TextInput(attrs={'class': 'form-control'}),
           
           'email': forms.EmailInput(attrs={'class': 'form-control'}),
            }
      
    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует")
        return super().clean()
    
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            )