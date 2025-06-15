from django import forms
from .models import Transaction, Category, Method, Profile
from django.contrib.auth.models import User

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'description', 'category', 'method']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
        
class MethodForm(forms.ModelForm):
    class Meta:
        model = Method
        fields = ['name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'user']  # Add 'image' field

    # Optionally, expose username and email via the user relation
    username = forms.CharField(max_length=150)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile.save()
        return profile

CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('EGP', 'Egyptian Pound'),
    ('GBP', 'British Pound'),
]

class PreferencesForm(forms.ModelForm):
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, label="Preferred Currency")

    class Meta:
        model = Profile
        fields = ['currency']