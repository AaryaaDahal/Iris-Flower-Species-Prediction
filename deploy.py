import streamlit as st
import joblib as jb

st.title("Iris Flower Species Prediction")

model = jb.load("model.joblib")
sp_length= st.number_input("Enter sepal length")
sp_width= st.number_input("Enter sepal width")
petal_length= st.number_input("Enter petal length")
petal_width= st.number_input("Enter petal width")

if (st.button("Predict")):
    pred = model.predict([[sp_length, sp_width, petal_length, petal_width]])[0]
    st.success(f"The predicted species is: {pred} ")
