from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def checkalpha(value):
    # if value.startswith("," | "!" | "." | "/" | "<" | ">" | "{"):
        # raise forms.ValidationError("This is invalid")
    if value.isalpha() == False:
        raise forms.ValidationError('This is Invalid.')

def checkuserame(value):
    if value.isalnum() == False:
        raise forms.ValidationError('Username should be alpha or digit only.!')
    # if value[1].isdigit() == True:
    #     raise forms.ValidationError("Username can't start start with dight!")


def checkemail(value):
    if User.objects.filter(email = value).exists():
        raise forms.ValidationError("This email is already taken try another")

class SignupForm(UserCreationForm):
    username = forms.CharField(validators=[checkuserame],max_length=50,min_length=4,
    widget= forms.TextInput(attrs={'class':'input'}),
    error_messages={'required':'Username is required '})
    password1 = forms.CharField(label = 'Enter Password:',
     widget = forms.PasswordInput(attrs={'class':'input'}),
     error_messages= {'required':'This Password is required'})
    password2 = forms.CharField(label = 'Password Again', widget = forms.PasswordInput(attrs={'class':'input'}),
     error_messages= {'required':'This Password  is required'})
    first_name = forms.CharField(validators=[checkalpha],
    widget = forms.TextInput(attrs={'class':'input'}),
     error_messages= {'required':'First Name is required'})
    last_name = forms.CharField(validators=[checkalpha],
    widget = forms.TextInput(attrs={'class':'input'}),
    error_messages= {'required':'Last Name is required'})
    email = forms.CharField(validators=[checkemail],
    widget = forms.EmailInput(attrs={'class':'input'}),
    error_messages= {'required':'This Email is required'})
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']


# class LoginForm()