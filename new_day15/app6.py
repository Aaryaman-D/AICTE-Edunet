import streamlit as st

st.title("Name Outputt!!!")
firstname = st.text_input("Enter your First Name :")
lastname = st.text_input("Enter your Last Name :")
age = st.text_input("Enter your Age :")
city = st.text_input("Enter your City :")
age = st.text_input("Enter your Age :")


if st.button("submit"):
    st.write("hello "+firstname)
    st.write("hello "+lastname)
    st.write("hello "+city)
    st.write("hello "+age)