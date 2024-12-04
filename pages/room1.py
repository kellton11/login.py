import streamlit as st
import matplotlib.pyplot as plt
import random
from io import BytesIO
import time
import webbrowser


#backgriund-pedro

st.markdown("""
       background-image: url("https://i.pinimg.com/736x/50/d0/73/50d073d2df00db56fad02ad55669c1b3.jpg")     
       background-colour: #blue    
            """)

# Configuração inicial da página

st.set_page_config(page_title="Sistema de Votação com Gráfico", layout="centered")

# Títulos e descrição
st.title("🗳️ Sistema de Votação")
st.write("Vote no seu candidato preferido! Cada usuário pode votar apenas uma vez.")

#estilo que eu nao sei se é antes ou depois das variaveis-pedro
#e que se caso nao der certo apague
#isso é um bgl para mover esteticamente
st.markdown("""
    .card: hover;
    .card-background {
            transform: scale(1.15), translateZ(0);
            background-size: 300px; 
            }        
            .card-grid: hover > .card: not(:hover) {
            transform: scale(.9);
            }
            filter: brightness(0.5), saturate(0), contrast(1.2), blur(20px);

            """)

# Variáveis de estado para armazenar votos
if "votos_candidato1" not in st.session_state:
    st.session_state.votos_candidato1 = 0

if "votos_candidato2" not in st.session_state:
    st.session_state.votos_candidato2 = 0

if "ja_votou" not in st.session_state:
    st.session_state.ja_votou = False

# Verifica se o usuário já votou
if st.session_state.ja_votou:
    st.warning("Você já votou! Obrigado por participar.")
else:

    #cor no botão, pode ser depois tambem:

 st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #C8A2C8; /* COR LILAS PADRAO */
        color: white; /* Cor do texto */
        border: #000000;  /* preto */
        padding: 10px 20px;
        text-align: center;
        font-size: 16px;
        border-radius: 5px; /* Bordas arredondadas */
        transition: background-color 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #45a049; /* Cor ao passar o mouse */
    }
    </style>
    """,
    unsafe_allow_html=True
)

    
    # Botões de votação
col1, col2 = st.columns(2)

with col1:
        if st.button("Votar no Candidato 1"):  
            st.session_state.votos_candidato1 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 1!")
 
with col2:
        if st.button("Votar no Candidato 2"):
            st.session_state.votos_candidato2 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 2!")


col3, col4 = st.columns(2)
#candidato 1

with col3:
    if st.button("Discurso do candidato 1:"):
        webbrowser.open("https://drive.google.com/file/d/1kQLq79oVjbr01VncLILsOYeNoUbamg9Z/view")

        #detalhes:´ do detalhe 

image_urls = ["https://i.pinimg.com/736x/b1/87/ef/b187efc751add02b1a8b46be309dee4d.jpg", "https://i.pinimg.com/736x/8c/a7/23/8ca7235a3f891eaf5232fdb425408f09.jpg", "https://i.pinimg.com/736x/5c/6f/a8/5c6fa89c9ae47e2aa0449f0dfd43ddd2.jpg"]

for img_url in image_urls:
    st.image(img_url, use_column_width=True)


    

st.markdown("""
    <div style="background-color: #f0f0f0; border-radius: 8px; padding: 20px; margin: 10px;">
        <h3>Cartão de Informações</h3>
        <p>Este é um exemplo de cartão interativo.</p>
    </div>
    """, unsafe_allow_html=True)

#canditado 2
with col4:
        if st.button("Discurso do candidato 2:"):
            webbrowser.open("https://drive.google.com/file/d/1qmZaOtp8vKijO7M4KoV5A4kBMBEaNaf4/view")
    #detalhe:

image_urls = ["https://i.pinimg.com/736x/09/fe/6f/09fe6fb4700b309422326d6a8e2f0c44.jpg", "https://i.pinimg.com/736x/03/1f/ca/031fca135891f47896e7a3f455cfb5bb.jpg", "https://i.pinimg.com/736x/e3/33/01/e33301f6130fbe1b0f2a20920907be6b.jpg"]

for img_url in image_urls:
    st.image(img_url, use_column_width=True)


# Exibir os totais de votos
st.markdown("---")
st.markdown(f"""
### Totais de votos:
- **Candidato 1:** {st.session_state.votos_candidato1}
- **Candidato 2:** {st.session_state.votos_candidato2}
""")

# Gráfico de votação
st.markdown("---")
st.title("📊 Gráfico de Votação em Tempo Real")

# Dados iniciais
candidatos = ["Candidato 1", "Candidato 2"]
votos = [
    st.session_state.votos_candidato1,
    st.session_state.votos_candidato2,
]

# Gerar gráfico como imagem
def plotar_grafico():
    fig, ax = plt.subplots()
    ax.bar(candidatos, votos, color=['blue', 'green'])
    ax.set_title("Votação - Quem está ganhando")
    ax.set_xlabel("Candidatos")
    ax.set_ylabel("Número de votos")
    # Converter gráfico para imagem
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Botão para exibir gráfico
if st.button("Atualizar Gráfico"):
    # Atualizar votos no gráfico
    votos = [
        st.session_state.votos_candidato1,
        st.session_state.votos_candidato2,
    ]
    grafico = plotar_grafico()
    st.image(grafico, caption="Gráfico de Votação", use_column_width=True)
