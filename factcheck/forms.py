from django import forms


class ClaimCheckForm(forms.Form):
    claim_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': "e.g. The Headmaster said 1st Captains don't have to do homework"
        }),
        label="Kuddus's Claim"
    )
    