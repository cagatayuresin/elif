from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.EmailInput, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


class FileUploadForm(forms.Form):
    file = forms.FileField()
