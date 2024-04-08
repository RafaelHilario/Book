import streamlit as st
from streamlit_extras.let_it_rain import rain 
st.title("Introduction")


rain(
        emoji="📔",
        font_size=40,
        falling_speed=5,
        animation_length="infinite",
    )
st.text("Sendo criado por rafael...")
st.image('legal.jpg')