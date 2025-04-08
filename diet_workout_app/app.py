import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("age_gender_activity_fitness_data.csv")
    return df

data = load_data()

st.title("Diet & Workout Recommender (with Dataset)")

# User inputs
age = st.number_input("Enter your age", min_value=8, max_value=90, step=1)
gender = st.selectbox("Select your gender", ["Male", "Female"])
activity_level = st.selectbox("Activity Level", ["Low", "Moderate", "High"])
fitness_goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])
diet_type = st.selectbox("Diet Preference", ["Veg", "Non Veg", "Vegan", "Keto"])

# Filter dataset to match user input
filtered_data = data[
    (data['Age'] == age) &
    (data['Gender'].str.lower() == gender.lower()) &
    (data['Activity Level'].str.lower() == activity_level.lower())
]

if st.button("Get Recommendation"):
    if not filtered_data.empty:
        row = filtered_data.iloc[0]
        st.success(f"📊 Found matched data in dataset:\n\nCalories: {row['Calories']}\nProtein: {row['Protein']}g\nCarbs: {row['Carbs']}g\nFats: {row['Fats']}g")
        
        # Optional: Recommend workouts/diets based on fitness_goal
        st.markdown("### 💪 Workout Plan")
        if fitness_goal == "Weight Loss":
            st.write("Cardio 3x/week, strength 2x/week, yoga 1x/week")
        elif fitness_goal == "Muscle Gain":
            st.write("Strength training 4-5x/week, protein-rich diet")
        else:
            st.write("Balanced mix of strength, cardio, and flexibility")

        st.markdown("### 🥗 Sample Meal Plan")
        st.write(f"Diet Type: {diet_type}")
        if diet_type == "Veg":
            st.write("Lunch: Lentil + brown rice + veggies")
        elif diet_type == "Non Veg":
            st.write("Lunch: Grilled chicken + quinoa + greens")
        elif diet_type == "Vegan":
            st.write("Lunch: Chickpea salad + tofu + avocado")
        elif diet_type == "Keto":
            st.write("Lunch: Eggs + cheese + low-carb veggies")
    else:
        st.error("No matching data found for the given inputs.")
