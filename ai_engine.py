# ai_engine.py

from config import BMI_OVERWEIGHT, BMI_UNDERWEIGHT


def infer_goal(bmi: float, user_goal: str) -> dict:
    """
    Infer the final fitness goal using BMI and user preference.

    Returns:
        dict with:
        - final_goal
        - reason (explainability)
    """

    # Case 1: User wants auto decision
    if user_goal == "Auto":
        if bmi >= BMI_OVERWEIGHT:
            return {
                "final_goal": "Fat Loss",
                "reason": "BMI indicates overweight category"
            }
        elif bmi <= BMI_UNDERWEIGHT:
            return {
                "final_goal": "Muscle Gain",
                "reason": "BMI indicates underweight category"
            }
        else:
            return {
                "final_goal": "Fitness",
                "reason": "BMI is within healthy range"
            }

    # Case 2: User explicitly chooses a goal
    return {
        "final_goal": user_goal,
        "reason": "User-selected goal overrides BMI logic"
    }
