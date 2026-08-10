def final_price(amount: float, discount_rate: float) -> float:
    """Return the price after discount."""

    if not 0 <= discount_rate <= 1:
        raise ValueError(
            "discount_rate must be between 0 and 1"
        )

    return round(amount * (1 - discount_rate), 2)
# Validate discount rate before calculation