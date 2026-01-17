import streamlit as st
import pickle
import numpy as np

# Charger le modèle
with open("logistic_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🔬 Prédiction du Cancer du Sein")

st.write("Entrez les 30 caractéristiques pour prédire le diagnostic.")

# Saisie utilisateur
features = []
labels = [
    "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean",
    "compactness_mean", "concavity_mean", "concave points_mean", "symmetry_mean", "fractal_dimension_mean",
    "radius_se", "texture_se", "perimeter_se", "area_se", "smoothness_se",
    "compactness_se", "concavity_se", "concave points_se", "symmetry_se", "fractal_dimension_se",
    "radius_worst", "texture_worst", "perimeter_worst", "area_worst", "smoothness_worst",
    "compactness_worst", "concavity_worst", "concave points_worst", "symmetry_worst", "fractal_dimension_worst"
]

for label in labels:
    value = st.number_input(f"{label}", value=0.0)
    features.append(value)

# Prédiction
if st.button("Prédire"):
    prediction = model.predict([features])
    st.success(f"Prédiction : {'Malin' if prediction[0] == 1 else 'Bénin'}")
