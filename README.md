# ⚡ QuickFit – AI-Powered Fitness Planner

QuickFit is a Streamlit-based AI fitness application designed specifically for students and beginners.  
It provides personalized workout plans, diet recommendations, calorie tracking, and progress monitoring using basic AI logic and fitness formulas.

---

## 📌 Problem Statement

Most fitness applications offer generic workout and diet plans that do not consider:
- Individual body metrics (BMI, BMR, calorie needs)
- Student lifestyle and budget constraints
- Cultural food habits (especially Indian diet)
- Limited workout resources (home, dumbbells, gym)

As a result, students struggle to follow consistent, effective, and affordable fitness routines.

---

## 💡 Proposed Solution

QuickFit solves this problem by offering:
- Personalized onboarding (name, age, gender, height, weight)
- BMI & BMR calculation
- Goal-based calorie targets (Fat Loss / Muscle Gain / Maintain)
- 30-Day fitness plan with start & end dates
- Daily check-in system
- Workout Engine based on available equipment:
  - Home
  - Dumbbells
  - Gym
- Simple login & signup system
- Clean, distraction-free UI built with Streamlit

---

## 🛠️ System Development Approach (Technology Used)

| Component | Technology |
|--------|-----------|
| Frontend | Streamlit |
| Backend Logic | Python |
| Data Handling | Pandas |
| Styling | Custom CSS |
| Authentication | Session-based (Streamlit) |
| Deployment | Streamlit Cloud |
| Version Control | Git & GitHub |

---

## ⚙️ Core Features

### 🔹 User Authentication
- Login & Signup system
- Session-based user handling

### 🔹 Onboarding Flow
- Name
- Age
- Gender
- Height & Weight
- Fitness goal selection

### 🔹 Health Calculations
- BMI (Body Mass Index)
- BMR (Basal Metabolic Rate)
- Daily calorie requirement based on activity level

### 🔹 30-Day Fitness Plan
- Auto-generated start & end date
- Goal-oriented routine
- Balanced workout and rest days

### 🔹 Dashboard
- Daily workout check-in ✔
- Progress tracking
- 30-day plan overview
- Workout engine selector

### 🔹 Workout Engine
Workout selection based on available equipment:
- 🏠 Home Workout
- 🏋️ Dumbbells
- 🏋️‍♂️ Gym

Each workout includes:
- Exercise name
- Sets & reps logging

---

## 🧮 Algorithms Used

### BMI Formula
BMI = weight (kg) / height² (m²)

### BMR Formula (Mifflin-St Jeor)

**Male**
BMR = 10W + 6.25H − 5A + 5

**Female**
BMR = 10W + 6.25H − 5A − 161

### Daily Calories
Daily Calories = BMR × Activity Factor

---

## 🚀 Deployment

The application is deployed using Streamlit Cloud.

Steps:
1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Select:
   - Branch: main
   - Main file: app.py
4. Deploy application

---

## 📁 Project Structure

QuickFit/
├── app.py  
├── style.css  
├── requirements.txt  
├── assets/  
│   ├── banner-bg.jpg  
│   ├── sidebar-banner.jpg  
│   └── logo.png  
├── ai_engine.py  
├── workout_engine.py  
├── diet_optimizer.py  
├── metabolism.py  
├── food_db.py  
├── utils.py  
└── README.md  

---

## 📊 Result

- Personalized fitness plans for each user
- Simple and interactive dashboard
- Improved workout consistency
- Practical diet & workout suggestions for students
- Clean and responsive UI

---

## 🔮 Future Scope

- Database integration (SQLite / Firebase)
- Mobile app version
- AI-based meal recommendations
- Wearable device integration
- Advanced progress analytics
- Coach & community features

---

## 📚 References

1. WHO – BMI Classification  
https://www.who.int/tools/growth-reference-data-for-5to19-years/indicators/bmi-for-age

2. Mifflin-St Jeor Equation  
https://www.healthline.com/nutrition/bmr-formula

3. Streamlit Documentation  
https://docs.streamlit.io/

4. Calorie & Nutrition Basics  
https://www.nhs.uk/live-well/healthy-weight/

5. Python Official Documentation  
https://docs.python.org/3/

---

## 👨‍💻 Author

Ashu Yadav  
Student | Python Developer | AI Enthusiast  

GitHub: https://github.com/Ashu101200
