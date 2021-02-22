from django import forms

class RealtorForm(forms.Form):
	name = forms.CharField(label = "Realtor Name", max_length = 200)
	photo = forms.FileField(required=False)
	description = forms.CharField(label = "Description", required=False)
	email = forms.EmailField(label = "Email", max_length = 50)
	phone = forms.CharField(label = "Phone", max_length = 20)
