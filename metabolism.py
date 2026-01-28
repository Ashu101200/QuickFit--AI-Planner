# metabolism.py

from config import ACTIVITY_MULTIPLIER, CALORIE_ADJUSTMENT


def calculate_daily_calories(bmr: float, goal: str) -> int:
    """
    Calculate daily calorie requirement based on goal.
    """
    calories = (
        bmr * ACTIVITY_MULTIPLIER[goal]
        + CALORIE_ADJUSTMENT[goal]
    )
    return int(calories)


def protein_target(goal: str, weight_kg: float) -> float:
    """
    Calculate daily protein requirement (grams).
    """
    if goal == "Muscle Gain":
        return round(weight_kg * 1.8, 1)
    elif goal == "Fat Loss":
        return round(weight_kg * 1.2, 1)
    else:  # Fitness
        return round(weight_kg * 1.4, 1)
