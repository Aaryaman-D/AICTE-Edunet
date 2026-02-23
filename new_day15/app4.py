import streamlit as st 

st.title("simple chatbot")

Question=st.text_input("Ask me anything")

if st.button("send"):
    if st.write("you asked what is java",Question):
        st.write("hi")

        