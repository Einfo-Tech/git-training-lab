"""Small training example used by the Git practice exercises."""


def final_price(amount: float, discount_rate: float) -> float:
    """Return the price after discount.

    The validation exercise asks trainees to ensure discount_rate is between
    0 and 1 before calculating the result.
    """
    return round(amount * (1 - discount_rate), 2)


# czx test
//def final_price(amount: float, discount_rate: float) -> float:
    """Return the price after discount.

    The validation exercise asks trainees to ensure discount_rate is between
    0 and 1 before calculating the result.
    """
    return round(amount * (1 - discount_rate), 2)
