from django import forms

class name(forms.Form):
    TestName = forms.CharField(max_length=100)
    StartDate = forms.DateField(required=False)

#for wizard
class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()

class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)