from django import forms

class Postform(forms.Form):
    stuName = forms.CharField(max_length=50,initial="",required=True)
    stuID = forms.CharField(max_length=10,initial="",required=True)
    stuSex= forms.CharField(max_length=2,initial="M",required=True)
    stuBirth= forms.DateField()
    stuEmail= forms.EmailField(max_length=100,initial="",required=False)
    stuPhone= forms.CharField(max_length=20,initial="",required=False)
    stuAddress= forms.CharField(max_length=255,initial="",required=False)

