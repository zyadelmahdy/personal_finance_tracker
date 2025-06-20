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
        fields = ['image', 'user'] 

    username = forms.CharField(max_length=150)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['username'].initial = self.instance.user.username
        # If the form is bound and not valid, reset the image field to the original
        if self.is_bound and not self.is_valid():
            self.fields['image'].initial = self.instance.image

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
            profile.save()
        return profile

CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('EGP', 'Egyptian Pound'),
    ('TRY', 'Turkish Lira'),
]

class PreferencesForm(forms.ModelForm):
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, label="Preferred Currency")

    class Meta:
        model = Profile
        fields = ['currency']