from django import forms

class Postform(forms.Form):
    UserAccount = forms.CharField(max_length=50,initial="",required=True)
    UserEmail= forms.EmailField(max_length=100,initial="",required=True)
    UserPassword= forms.CharField(max_length=100,initial="",required=True)
    UserFirstName= forms.CharField(max_length=50,initial="",required=True)
    UserLastName= forms.CharField(max_length=50,initial="",required=True)

