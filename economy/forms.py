from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'amount_taka', 'food_item', 'estimated_calories']
        widgets = {
            'amount_taka': forms.NumberInput(attrs={'placeholder': 'e.g. 2 (for washroom toll)'}),
            'food_item': forms.TextInput(attrs={'placeholder': 'e.g. Fried Rice, Sandwich'}),
            'estimated_calories': forms.NumberInput(attrs={'placeholder': 'e.g. 350'}),
        }