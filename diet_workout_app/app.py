import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    height_m = height / 100  # Convert cm to meters
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

def generate_recommendations():
    age = int(age_entry.get())
    gender = gender_var.get()
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    fitness_goal = goal_var.get()
    diet_type = diet_var.get()
    
    bmi = calculate_bmi(weight, height)
    bmr = calculate_bmr(weight, height, age, gender)
    diet_plan = recommend_diet(fitness_goal, bmr, diet_type)
    workout_plan = recommend_workout(fitness_goal)
    
    result_text = f"BMI: {bmi}\nBMR: {bmr} kcal/day\n\n🥗 Recommended Diet:\n{diet_plan}\n🏋️ Workout Plan:\n{workout_plan}"  
    messagebox.showinfo("Results", result_text)

root = tk.Tk()
root.title("Diet & Workout Recommender")
root.geometry("400x700")

tk.Label(root, text="Enter your details", font=("Arial", 14)).pack()

# Age
age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Gender
gender_var = tk.StringVar(value="Male")
tk.Label(root, text="Gender:").pack()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

# Height
height_label = tk.Label(root, text="Height (cm):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Weight
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Fitness Goal
goal_var = tk.StringVar(value="Weight Loss")
tk.Label(root, text="Fitness Goal:").pack()
tk.OptionMenu(root, goal_var, "Weight Loss", "Muscle Gain", "Maintenance").pack()

# Diet Type
diet_var = tk.StringVar(value="Veg")
tk.Label(root, text="Diet Preference:").pack()
tk.OptionMenu(root, diet_var, "Veg", "Non Veg", "Vegan", "Keto").pack()

# Submit Button
tk.Button(root, text="Get Recommendation", command=generate_recommendations).pack()

root.mainloop()
