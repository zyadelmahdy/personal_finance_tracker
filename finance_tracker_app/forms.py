from django import forms
from .models import Transaction, Category, Method

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