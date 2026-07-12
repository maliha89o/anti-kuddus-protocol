from django.db import models


class Transaction(models.Model):
    TYPE_CHOICES = [
        ('cash', 'Cash Extortion (Washroom Toll)'),
        ('food', 'Stolen Food/Tiffin'),
    ]

    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount_taka = models.PositiveIntegerField(default=0, help_text="Taka amount (for cash type)")
    food_item = models.CharField(max_length=100, blank=True, help_text="Food item name (for food type)")
    estimated_calories = models.PositiveIntegerField(default=0, help_text="Estimated calories of the food item")
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.transaction_type == 'cash':
            return f"Cash: {self.amount_taka} Taka"
        return f"Food: {self.food_item} ({self.estimated_calories} cal)"