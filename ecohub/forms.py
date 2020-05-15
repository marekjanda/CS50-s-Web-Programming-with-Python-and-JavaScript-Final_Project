from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime
from tinymce import TinyMCE, HTMLField
from tinymce.widgets import TinyMCE
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

from .models import NewsCategory

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                    'email', 'password1', 'password2',)


class BlogForm(forms.Form):
    category = forms.ModelChoiceField(queryset=NewsCategory.objects.all(), empty_label="--Select Category--")
    title = forms.CharField(max_length=255)
    abstract = forms.CharField(widget=TinyMCE(mce_attrs={'height': 150}))
    content = forms.CharField(widget=TinyMCE(mce_attrs={'height': 500}))

class ProjectForm(forms.Form):
    category = forms.ModelChoiceField(queryset=NewsCategory.objects.all(), empty_label="--Select Category--")
    title = forms.CharField(max_length=255)
    abstract = forms.CharField(widget=TinyMCE(mce_attrs={'height': 150}))
    description = forms.CharField(widget=TinyMCE(mce_attrs={'height': 500}))
    target_funds = forms.IntegerField()
    attachment = forms.FileField(required=False)

class ContactForm(forms.Form):
    SUBJECTS = (
        ('more', 'More information'),
        ('collaboration', 'Collaboration offer'),
        ('join', 'Join Project'),
        ('invest', 'Make investment'),
        ('advertise', 'Advertisement'),
        ('other', 'Other business offer'),
    )
    subject = forms.ChoiceField(choices=SUBJECTS)
    message = forms.Textarea()