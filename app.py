import streamlit as st
import pandas as pd
from datetime import date, timedelta

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="QuickFit", page_icon="⚡", layout="wide")

# --------------------------------------------------
# SESSION STATE INIT
# --------------------------------------------------
for key, default in {
    "logged_in": False,
    "user_db": {},
    "current_user": None,
    "step": 1,
    "profile": {},
    "checkin": [False]*30,
    "workout_log": {}
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# --------------------------------------------------
# AUTH SYSTEM
# --------------------------------------------------
def signup():
    st.subheader("📝 Signup")

    u = st.text_input("Username", key="signup_username")
    p = st.text_input("Password", type="password", key="signup_password")

    if st.button("Create Account", key="signup_btn"):
        if u in st.session_state.user_db:
            st.error("User already exists")
        else:
            st.session_state.user_db[u] = p
            st.success("Account created! Please login.")


def login():
    st.subheader("🔐 Login")

    u = st.text_input("Username", key="login_username")
    p = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_btn"):
        if st.session_state.user_db.get(u) == p:
            st.session_state.logged_in = True
            st.session_state.current_user = u
            st.success("Logged in successfully")
            st.rerun()
        else:
            st.error("Invalid credentials")


# --------------------------------------------------
# LOGIN SCREEN
# --------------------------------------------------
if not st.session_state.logged_in:
    st.title("⚡ QuickFit")
    tab1, tab2 = st.tabs(["Login", "Signup"])
    with tab1:
        login()
    with tab2:
        signup()
    st.stop()

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(f"""
<div style="text-align:center;">
<h1>⚡ Quick<span style="color:#ffaa00;">Fit</span></h1>
<p>Smart Fitness for Real Life</p>
<p>Welcome, <b>{st.session_state.current_user}</b></p>
</div>
""", unsafe_allow_html=True)

st.progress(st.session_state.step / 6)

# --------------------------------------------------
# STEP 1 – BASIC INFO
# --------------------------------------------------
if st.session_state.step == 1:
    st.subheader("👋 Basic Details")
    name = st.text_input("Name")
    age = st.number_input("Age", 10, 80)

    if st.button("Next →"):
        st.session_state.profile.update({"name": name, "age": age})
        st.session_state.step = 2
        st.rerun()

# --------------------------------------------------
# STEP 2 – BODY DETAILS
# --------------------------------------------------
elif st.session_state.step == 2:
    gender = st.radio("Gender", ["Male", "Female"])
    height = st.number_input("Height (cm)", 120, 220)
    weight = st.number_input("Weight (kg)", 30, 200)

    if st.button("Next →"):
        st.session_state.profile.update({
            "gender": gender,
            "height": height,
            "weight": weight
        })
        st.session_state.step = 3
        st.rerun()

# --------------------------------------------------
# STEP 3 – BMI & BMR
# --------------------------------------------------
elif st.session_state.step == 3:
    p = st.session_state.profile
    bmi = p["weight"] / ((p["height"]/100)**2)

    if p["gender"] == "Male":
        bmr = 10*p["weight"] + 6.25*p["height"] - 5*p["age"] + 5
    else:
        bmr = 10*p["weight"] + 6.25*p["height"] - 5*p["age"] - 161

    st.metric("BMI", round(bmi, 2))
    st.metric("BMR", int(bmr))

    p.update({"bmi": bmi, "bmr": bmr})

    if st.button("Next →"):
        st.session_state.step = 4
        st.rerun()

# --------------------------------------------------
# STEP 4 – GOAL & CALORIES
# --------------------------------------------------
elif st.session_state.step == 4:
    goal = st.radio("Goal", ["Fat Loss", "Maintain", "Muscle Gain"])
    activity = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active"])

    factor = {"Sedentary":1.2,"Light":1.375,"Moderate":1.55,"Active":1.725}[activity]
    calories = st.session_state.profile["bmr"] * factor
    if goal == "Fat Loss": calories -= 500
    if goal == "Muscle Gain": calories += 300

    st.metric("Daily Calories", int(calories))
    st.session_state.profile.update({"goal": goal, "calories": int(calories)})

    if st.button("Go to Dashboard →"):
        st.session_state.step = 5
        st.rerun()

# --------------------------------------------------
# STEP 5 – DASHBOARD
# --------------------------------------------------
elif st.session_state.step == 5:
    p = st.session_state.profile
    start = date.today()
    end = start + timedelta(days=29)

    st.subheader("📅 30-Day Fitness Plan")
    st.write(f"Start: {start} | End: {end}")

    # DAILY CHECK-IN
    st.subheader("✅ Daily Check-in")
    completed = 0
    for i in range(30):
        st.session_state.checkin[i] = st.checkbox(f"Day {i+1}", st.session_state.checkin[i])
        if st.session_state.checkin[i]:
            completed += 1
    st.success(f"Completed: {completed}/30 days")

    # PROGRESS
    st.subheader("📈 Progress")
    df = pd.DataFrame({"Day": range(1,31), "Weight": [p["weight"]]*30})
    st.line_chart(df.set_index("Day"))

    # DIET
    st.subheader("🥗 Diet Plan")
    if p["goal"] == "Fat Loss":
        diet = ["Oats", "Dal-Roti", "Veg + Paneer"]
    elif p["goal"] == "Muscle Gain":
        diet = ["Eggs/Paneer", "Rice + Dal", "Protein Dinner"]
    else:
        diet = ["Balanced Indian Meals"]
    for d in diet:
        st.write("•", d)

    # WORKOUT ENGINE
    st.subheader("🏋️ Workout Engine (Reps & Sets)")
    mode = st.selectbox("Workout Type", ["Home", "Dumbbells", "Gym"])

    workout_map = {
        "Home": ["Pushups", "Squats", "Plank"],
        "Dumbbells": ["Bicep Curl", "Shoulder Press"],
        "Gym": ["Bench Press", "Lat Pulldown", "Leg Press"]
    }

    today = str(date.today())
    if today not in st.session_state.workout_log:
        st.session_state.workout_log[today] = {}

    for ex in workout_map[mode]:
        sets = st.number_input(f"{ex} - Sets", 1, 10, 3, key=ex+"s")
        reps = st.number_input(f"{ex} - Reps", 1, 30, 10, key=ex+"r")
        st.session_state.workout_log[today][ex] = {"sets": sets, "reps": reps}

    st.success("Workout Logged Successfully")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<hr>
<div style="text-align:center; color:gray;">
⚡ QuickFit · AI Powered · Student Focused · Budget Aware
</div>
""", unsafe_allow_html=True)
