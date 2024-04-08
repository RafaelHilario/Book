import streamlit as st
st.title("Books")

def favoritos():
    lista = st.selectbox(
        'Qual livro favorito você vai escolher?',
        ('Petter pan', 'Viagem ao centro da terra', 'outsider'),
        index=None,
    placeholder="Select contact method...")



    if lista == 'Petter pan':
        st.write('Você selecionou petter pan:')
        st.image("pan.jpg")

        st.write('Quer saber mais sobre petter pan? clique abaixo')
        st.link_button("Clique aqui", "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://pt.wikipedia.org/wiki/Peter_Pan&ved=2ahUKEwik6uuBm7OFAxXSpJUCHYY2DjkQFnoECCwQAQ&usg=AOvVaw2bIKKQ4WlqIK7UCQm8kNrr")

    if lista == 'Viagem ao centro da terra':
        st.write('Você selecionou Viagem ao centro da terra')
        st.image("viagem.jpg")
        st.write("Quer saber mais sobre a incrivel viagem? clique abaixo")
        st.link_button("Clique aqui", "https://www.amazon.com.br/Viagem-Centro-Terra-Jules-Verne/dp/8537815519/ref=pd_lpo_sccl_2/132-9631722-3327767?pd_rd_w=lXoVu&content-id=amzn1.sym.8151c21e-945b-4095-a73d-67d730c81d28&pf_rd_p=8151c21e-945b-4095-a73d-67d730c81d28&pf_rd_r=CSA2CAYC0BMP189TN78R&pd_rd_wg=hN3B6&pd_rd_r=593b94c0-998a-4185-992c-23a68eec027f&pd_rd_i=8537815519&psc=1")

    if lista == "outsider":
        st.write("Você selecionou outsider")
        st.image("outside.jpg")
        st.write("Quer saber mais sobre a incrivel obra de Stephen King? Clique abaixo")
        st.link_button("Clique aqui", "https://www.amazon.com.br/Outsider-Stephen-King/dp/8556510671")

favoritos()