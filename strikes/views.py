from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RollNumberForm, ComplaintForm
from .models import Complaint, RollNumberHash


def roll_login(request):
    """
    Roll number diye 'login' - kono actual user account na,
    shudhu ekta known/allowed roll number list check kore
    session e mark kore rakhi 'verified student' hisebe.
    """
    if request.method == 'POST':
        form = RollNumberForm(request.POST)
        if form.is_valid():
            roll = form.cleaned_data['roll_number']
            if roll.strip():
                request.session['verified_roll'] = True
                return redirect('submit_complaint')
            messages.error(request, "Shothik Roll Number dao")
    else:
        form = RollNumberForm()
    return render(request, 'strikes/roll_login.html', {'form': form})


def submit_complaint(request):
    if not request.session.get('verified_roll'):
        messages.error(request, "Age Roll Number diye verify koro")
        return redirect('roll_login')

    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save()
            request.session['verified_roll'] = False
            messages.success(request, "Complaint jomeche! Dhonnobad tomar shahoshikotar jonno.")
            return redirect('strikes_dashboard')
    else:
        form = ComplaintForm()
    return render(request, 'strikes/submit_complaint.html', {'form': form})


def dashboard(request):
    total_strikes = Complaint.objects.filter(is_verified_strike=True).count()
    context = {
        'total_strikes': total_strikes,
        'strikes_remaining': max(0, 3 - total_strikes),
        'progress_percent': min(100, (total_strikes / 3) * 100),
    }
    return render(request, 'strikes/dashboard.html', context)