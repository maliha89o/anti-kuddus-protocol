from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'amount_taka', 'food_item', 'estimated_calories', 'logged_at')
    list_filter = ('transaction_type',)