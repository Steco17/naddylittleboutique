from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"fullname","name":"fullname","placeholder":"Your Full name",}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","id":"email","name":"email","placeholder":"Your Email",}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","id":"content","name":"content","placeholder":"Your Message",}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email