from django import forms

class ReplyEmailForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=1000, widget=forms.Textarea)