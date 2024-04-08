import streamlit as st
from streamlit_extras.let_it_rain import rain 
st.title("Introduction")

def example():
    rain(
        emoji="📔",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
example()