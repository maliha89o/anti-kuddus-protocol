from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TransactionForm
from .models import Transaction
from .logic import calculate_totals, convert_to_weaponry


def log_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction logged successfully!")
            return redirect('economy_dashboard')
    else:
        form = TransactionForm()

    return render(request, 'economy/log_transaction.html', {'form': form})


def economy_dashboard(request):
    transactions = Transaction.objects.all()
    totals = calculate_totals(transactions)
    weaponry = convert_to_weaponry(totals['total_cash'])

    context = {
        'transactions': transactions.order_by('-logged_at')[:10],
        'totals': totals,
        'weaponry': weaponry,
    }
    return render(request, 'economy/dashboard.html', context)