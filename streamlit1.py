import streamlit as st
st.title("welcome")
st.header("this is jayasri")
st.caption("this is for choosing your favour colr")
radio = st.radio("what is your fav color ?"  ,( 'white','safron','orange'))
st.write("your fav color is ", radio)
