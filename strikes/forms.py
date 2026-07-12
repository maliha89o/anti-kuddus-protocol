from django import forms
from .models import Complaint


class RollNumberForm(forms.Form):
    roll_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'Tomar Roll Number',
            'class': 'roll-input'
        })
    )


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['category', 'description', 'evidence_image']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Ki hoyeche bistarito likho...'
            }),
        }