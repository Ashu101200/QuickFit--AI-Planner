# diet_optimizer.py

from food_db import FOOD_DB


def optimize_diet(
    calorie_target: int,
    protein_target: float,
    budget: int,
    food_pref: str,
    calorie_tolerance: float = 0.05
) -> dict:
    """
    Constraint-based diet optimizer.
    """

    allowed_foods = []
    for food, data in FOOD_DB.items():
        if food_pref == "Veg" and not data["veg"]:
            continue
        allowed_foods.append((food, data))

    allowed_foods.sort(key=lambda x: x[1]["cost"])

    selected = []
    total_cal = 0
    total_protein = 0
    total_cost = 0

    for food, data in allowed_foods:
        if total_cost + data["cost"] > budget:
            continue

        selected.append(food)
        total_cost += data["cost"]
        total_cal += data["calories"]
        total_protein += data["protein"]

        if (
            total_cal >= calorie_target * (1 - calorie_tolerance)
            and total_protein >= protein_target
        ):
            break

    return {
        "foods": selected,
        "total_calories": total_cal,
        "total_protein": round(total_protein, 1),
        "total_cost": total_cost,
        "within_budget": total_cost <= budget,
        "calorie_target_met": total_cal >= calorie_target * (1 - calorie_tolerance),
        "protein_target_met": total_protein >= protein_target
    }
    workout_plan = generate_workout_plan(equipment, time_minutes)
