from django import forms
from .models import Employee

class MemberForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"uk-input","placeholder":"First name","name":"firstname"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"uk-input","placeholder":"Last name","name":"lastname"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"uk-input","placeholder":"E-mail","name":"emailid"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"class":"uk-input","placeholder":"Phone number","name":"phone"}))
    class Meta:
        model = Employee
        fields = ["first_name","last_name","email","phone_number"]

class MemberEditForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"uk-input","placeholder":"First name","name":"firstname","id":"edit_firstname"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"uk-input","placeholder":"Last name","name":"lastname","id":"edit_lastname"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"uk-input","placeholder":"E-mail","name":"emailid","id":"edit_emailid"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"class":"uk-input","placeholder":"Phone number","name":"phone","id":"edit_phone"}))
    class Meta:
        model = Employee
        fields = ["first_name","last_name","email","phone_number"]