from django import forms


class SyllabusInputForm(forms.Form):
    raw_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 8,
            'placeholder': "Paste Kuddus's syllabus statement here..."
        }),
        label="Syllabus Statement"
    )
    days_remaining = forms.IntegerField(
        initial=7,
        min_value=1,
        max_value=30,
        label="How many days remain until the test?"
    )