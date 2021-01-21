from django import forms
from .models import Shortener

class ShortenerForm(forms.ModelForm):
	class Meta:
		model = Shortener
		fields = ['url']

# class ShortenerForm(forms.Form):
# 	url = forms.CharField(label="URL", max_length=200)
