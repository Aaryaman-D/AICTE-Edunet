import streamlit as st

st.title("Basic Calculator")

num1 = st.number_input("Enter your First Number :")
num2 = st.number_input("Enter your Second Number :")

operation=st.selectbox("Select your operation:",["Add","Subtract","Multiply","Divide"])
if operation=="Add":
    st.write(num1+num2)
elif operation=="Subtract":
    st.write(num1-num2)
elif operation=="Multiply":
    st.write(num1*num2)
elif operation=="Divide":
    if num2!=0:
        st.write(num1/num2)
else:
    st.write("")


    # if st.button("+"):
#     st.write(num1+num2)
# if st.button("-"):
#     st.write(num1-num2)
# if st.button("*"):
#     st.write(num1*num2)
# if st.button("/"):
#     st.write(num1/num2)
