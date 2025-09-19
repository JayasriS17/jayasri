# %%writefile app.py
import streamlit as st
import joblib
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib
import numpy as np

# Train a model
X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model with joblib.dump

# Load model
model = joblib.load("model.joblib")       #< -- load



# Streamlit UI
st.title("🌸 Iris Flower Prediction App")
st.write("Enter flower measurements to predict species")

# User inputs
sepal_length = st.number_input("Sepal Length", min_value=0.0, step=0.1)
sepal_width  = st.number_input("Sepal Width", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length", min_value=0.0, step=0.1)
petal_width  = st.number_input("Petal Width", min_value=0.0, step=0.1)

# Predict button
if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    st.success(f"🌼 Predicted Species: {prediction}")
