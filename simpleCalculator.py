import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter first number:")
operator = st.selectbox("Select operator", ["+", "-", "*", "/"])
num2 = st.number_input("Enter second number:")

if st.button("Calculate"):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            result = "Error: Cannot divide by zero"
        else:
            result = num1 / num2
    else:
        result = "Invalid operator"

    st.success(f"Result: {result}")

