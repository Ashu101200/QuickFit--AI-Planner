# workout_engine.py

def generate_workout_plan(equipment: str, time_minutes: int) -> list:
    """
    Generate a 7-day workout plan based on equipment and time.
    """

    workouts = {
        "None": [
            "Jumping Jacks",
            "Bodyweight Squats",
            "Push-ups",
            "Plank",
            "Mountain Climbers"
        ],
        "Dumbbells": [
            "Dumbbell Squats",
            "Dumbbell Shoulder Press",
            "Dumbbell Rows",
            "Dumbbell Bicep Curl",
            "Dumbbell Tricep Extension"
        ],
        "Gym": [
            "Chest + Triceps",
            "Back + Biceps",
            "Legs",
            "Shoulders",
            "Core",
            "Cardio"
        ]
    }

    base_workout = workouts[equipment]

    plan = []

    for day in range(1, 8):
        if day == 7:
            plan.append("Rest / Active Recovery (Stretching, Walking)")
        else:
            intensity = (
                "Light" if day <= 2
                else "Moderate" if day <= 5
                else "High"
            )

            exercises = ", ".join(base_workout[:3])
            plan.append(
                f"Day {day}: {exercises} | Intensity: {intensity} | Time: {time_minutes} min"
            )

    return plan
    st.subheader("7-Day Workout Plan")

    for day in workout_plan:
        st.write(day)
       