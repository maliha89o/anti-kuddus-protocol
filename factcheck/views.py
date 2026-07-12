from django.shortcuts import render
from .forms import ClaimCheckForm
from .logic import check_claim


def fact_checker(request):
    result = None

    if request.method == 'POST':
        form = ClaimCheckForm(request.POST)
        if form.is_valid():
            claim = form.cleaned_data['claim_text']
            result = check_claim(claim)
    else:
        form = ClaimCheckForm()

    return render(request, 'factcheck/checker.html', {
        'form': form,
        'result': result,
    })