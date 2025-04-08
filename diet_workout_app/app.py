
import streamlit as st
import joblib
import numpy as np

st.title("💪 Personalized Diet & Workout Recommender")

age = st.slider("Age", 8, 90, 25)
gender = st.selectbox("Gender", ["Male", "Female"])
activity = st.selectbox("Activity Level", ["Low", "Medium", "High"])
height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)

# Load models
model_workout = joblib.load("model_workout.pkl")
model_diet = joblib.load("model_diet.pkl")
label_encoders = joblib.load("label_encoders.pkl")
scaler = joblib.load("scaler.pkl")

if st.button("Get My Recommendations"):
    gender_encoded = label_encoders["Gender"].transform([gender])[0]
    activity_encoded = label_encoders["Activity_Level"].transform([activity])[0]
    input_data = np.array([[age, gender_encoded, activity_encoded, height, weight]])
    input_scaled = scaler.transform(input_data[:, [0, 3, 4]])

    workout_pred = model_workout.predict(np.array([[age, gender_encoded, activity_encoded]]))[0]
    diet_pred = model_diet.predict(np.array([[age, gender_encoded, activity_encoded]]))[0]

    st.success(f"🏋️ Recommended Workout Plan: {workout_pred}")
    st.success(f"🥗 Recommended Diet Plan: {diet_pred}")
