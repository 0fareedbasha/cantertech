import streamlit as st
import streamlit_analytics


with streamlite_analytics.track():
    st.text_input("write your name")
    st.selectbox("select your favorite",["guvi","data","science"])
    st.button("click me")
