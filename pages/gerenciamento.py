import streamlit as st
import time
st.title("Gerenciamento")

lista_terror = ["Outsider"]
lista_suspense = ["Viagem ao centro da terra"]
lista_magia = ["Petter pan"]
lista_aventura = ["Petter pan"]

genero = st.selectbox(
        'Qual Gênero de livro você gosta?',
        ('Terror', 'Suspense', 'Magia', 'Aventura', 'Outro'),
        index=None,
    placeholder="Selecione o gênero...")

with st.container(height=700, border=500):
    if genero == 'Terror':
        st.image("outside.jpg")
    st.image("viagem.jpg")
    st.image("pan.jpg")

