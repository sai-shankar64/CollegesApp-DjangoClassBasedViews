from django import forms
class SignUpForm(forms.Form):
        first_name=forms.CharField(
            max_length=50,
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter FirstName'})
        )
        last_name=forms.CharField(
            max_length=30,
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter LastName'})
        )
        username=forms.CharField(
            max_length=30,
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
        )
        password=forms.CharField(
            max_length=100,
            required=True,
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
        )

class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )
    password=forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'})
    )