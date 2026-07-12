CRICKET_BAT_PRICE_TAKA = 1500
JHALMURI_PACKET_PRICE_TAKA = 20


def calculate_totals(transactions):
    total_cash = sum(t.amount_taka for t in transactions if t.transaction_type == 'cash')
    total_calories = sum(t.estimated_calories for t in transactions if t.transaction_type == 'food')
    food_count = transactions.filter(transaction_type='food').count()

    return {
        'total_cash': total_cash,
        'total_calories': total_calories,
        'food_count': food_count,
        'kinetic_output': 0,  # Kuddus's indoor Ludu lifestyle means zero energy spent
        'caloric_disparity': total_calories,  # since kinetic output is always 0
    }


def convert_to_weaponry(total_cash):
    """
    Advanced: Converts extorted cash into relatable metrics -
    how many cricket bats or jhalmuri packets could be funded.
    """
    cricket_bats = total_cash // CRICKET_BAT_PRICE_TAKA
    jhalmuri_packets = total_cash // JHALMURI_PACKET_PRICE_TAKA

    return {
        'cricket_bats': cricket_bats,
        'jhalmuri_packets': jhalmuri_packets,
    }