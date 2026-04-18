import streamlit as st
st.title("BMI Calculator")
height = st.slider("Enter your height (in cm)", 100, 220)
weight = st.slider("Enter your weight (in kg)", 30, 150)
if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.subheader(f"Your BMI is: {round(bmi, 2)}")
    if bmi < 18.5:
        st.warning("You are underweight")
    elif 18.5 <= bmi < 25:
        st.success("You have a normal weight")
    elif 25 <= bmi < 30:
        st.warning("You are overweight")
    else:
        st.error("You are obese")
