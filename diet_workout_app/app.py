import streamlit as st

def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    return round(bmr, 2)

def recommend_diet(fitness_goal, bmr, diet_type):
    if fitness_goal.lower() == 'weight loss':
        calories = bmr - 500
        macros = {'Protein': 0.4, 'Carbs': 0.4, 'Fats': 0.2, 'Fiber': 30}
    elif fitness_goal.lower() == 'muscle gain':
        calories = bmr + 500
        macros = {'Protein': 0.3, 'Carbs': 0.5, 'Fats': 0.2, 'Fiber': 35}
    else:
        calories = bmr
        macros = {'Protein': 0.3, 'Carbs': 0.45, 'Fats': 0.25, 'Fiber': 30}

    protein_grams = round((macros['Protein'] * calories) / 4, 2)
    carbs_grams = round((macros['Carbs'] * calories) / 4, 2)
    fats_grams = round((macros['Fats'] * calories) / 9, 2)
    fiber_grams = macros['Fiber']

    meal_plans = {
        "Veg": {
            "Breakfast": "Oatmeal with nuts and fruits",
            "Lunch": "Lentil soup with brown rice and vegetables",
            "Dinner": "Grilled paneer with quinoa and salad",
            "Snacks": "Greek yogurt with almonds"
        },
        "Non Veg": {
            "Breakfast": "Egg omelette with whole wheat toast",
            "Lunch": "Grilled chicken with sweet potatoes and greens",
            "Dinner": "Salmon with steamed vegetables and quinoa",
            "Snacks": "Boiled eggs with mixed nuts"
        },
        "Vegan": {
            "Breakfast": "Smoothie with banana, almond milk, and chia seeds",
            "Lunch": "Quinoa salad with chickpeas and avocado",
            "Dinner": "Tofu stir-fry with brown rice",
            "Snacks": "Hummus with carrot and cucumber sticks"
        },
        "Keto": {
            "Breakfast": "Scrambled eggs with avocado and cheese",
            "Lunch": "Grilled chicken with cauliflower rice and greens",
            "Dinner": "Steak with asparagus and butter",
            "Snacks": "Cheese and almonds"
        }
    }

    diet_plan = f"Calories: {calories} kcal\nProtein: {protein_grams}g\nCarbs: {carbs_grams}g\nFats: {fats_grams}g\nFiber: {fiber_grams}g\n\n🍽 Meal Plan:\n"
    for meal, food in meal_plans[diet_type].items():
        diet_plan += f"{meal}: {food}\n"

    return diet_plan

def recommend_workout(fitness_goal):
    workout_plans = {
        "Weight Loss": ["Monday: Cardio + HIIT", "Tuesday: Strength Training", "Wednesday: Yoga", "Thursday: Cardio", "Friday: Strength Training", "Saturday: Full-body Workout", "Sunday: Rest"],
        "Muscle Gain": ["Monday: Chest & Triceps", "Tuesday: Back & Biceps", "Wednesday: Rest", "Thursday: Legs & Abs", "Friday: Shoulders & Arms", "Saturday: Full-body Workout", "Sunday: Rest"],
        "Maintenance": ["Monday: Full-body Strength", "Tuesday: Cardio", "Wednesday: Yoga", "Thursday: Strength Training", "Friday: Cardio & Abs", "Saturday: Mobility & Stretching", "Sunday: Rest"]
    }
    return "\n".join(workout_plans.get(fitness_goal, []))

st.title("💪 Diet & Workout Recommender")

age = st.number_input("Enter your Age", min_value=8, max_value=100, step=1)
gender = st.radio("Select Gender", ["Male", "Female"])
height = st.number_input("Height (in cm)")
weight = st.number_input("Weight (in kg)")
fitness_goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])
diet_type = st.selectbox("Diet Preference", ["Veg", "Non Veg", "Vegan", "Keto"])

if st.button("Get Recommendations"):
    bmi = calculate_bmi(weight, height)
    bmr = calculate_bmr(weight, height, age, gender)
    diet_plan = recommend_diet(fitness_goal, bmr, diet_type)
    workout_plan = recommend_workout(fitness_goal)

    st.success(f"Your BMI: {bmi}\nYour BMR: {bmr} kcal/day")
    st.markdown(f"### 🥗 Diet Plan\n{diet_plan}")
    st.markdown(f"### 🏋️ Workout Plan\n{workout_plan}")
