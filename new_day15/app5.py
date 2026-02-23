import streamlit as st

st.markdown(''' 
<style>
.stButton>button{
    background-color:green;
    color:white;
    border-radius:50%;
}
</style>
''',unsafe_allow_html=True)

st.title("Welcome to Streamlit App !")
age = st.slider("Select your age :",1,100)
city = st.selectbox("Select your City ",["Delhi","Mumbai","Nashik","Pune","NYC"])

if st.button("SHOW DETAILS"):
    st.write("Age : ",age)
    st.write("City : ",city)