# grocery/forms.py
from django import forms
from .models import GroceryTransaction

class GroceryTransactionForm(forms.ModelForm):
    class Meta:
        model = GroceryTransaction
        fields = ['item', 'quantity']
