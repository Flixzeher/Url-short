from .models import ShortUrl
from django import forms

class CreateNewShortURL(forms.Form):
    original_url = forms.URLField(label='Original URL', max_length=200)
    custom_short_url = forms.CharField(label='Custom Short URL', max_length=50, required=False)