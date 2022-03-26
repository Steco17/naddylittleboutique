from django import forms
from django.contrib.auth import get_user_model


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"fullname","name":"fullname","placeholder":"Your Full name",}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","id":"email","name":"email","placeholder":"Your Email",}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","id":"content","name":"content","placeholder":"Your Message",}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"username","name":"username","placeholder":"Your User Name",}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","id":"password","name":"password","placeholder":"Your Password",}))


class RegisterForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailInput()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput)

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
            
        return data
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.object.filter(username= username)
        if qs.excists():
             raise forms.ValidationError("User Name Already Exixts..")
        
        return data
    
    def clean_email(self):
        username = self.cleaned_data.get('email')
        qs = User.object.filter(email= email)
        if qs.excists():
             raise forms.ValidationError("User Email Already Exixts..")
        
        return data
        
       