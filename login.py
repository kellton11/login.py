import streamlit as st
import base64
from time import sleep

def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str

def cadastro():
    background_image_path = "img/login.jpeg"  # Certifique-se de que o caminho está correto
    background_image = get_base64_image(background_image_path)

    st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{background_image}"); 
            background-size: cover;
            background-position: center; 
            background-attachment: fixed; 
        }}
    </style>
    """, unsafe_allow_html=True)


st.sidebar.image("img/vote.jpeg")
# Chamada da função para carregar o fundo
cadastro()

def ver_preenchidos(campos):
    return all(campos.values())

# Informações sobre o aluno
foto = st.file_uploader("Foto do aluno:", type=["jpg", "jpeg", "png"])
nome = st.text_input("Nome do aluno:", value="", placeholder="Digite aqui...")
cpf = st.text_input("CPF do aluno:", value="", placeholder="Digite aqui...")
responsavel = st.text_input("Responsável do aluno:", value="", placeholder="Digite aqui...")
id_es = st.text_input("Número ID da escola:", value="", placeholder="Digite aqui...")

if foto is not None:
    st.image(foto, caption="Foto do aluno", width=100)

# IDs das escolas
ids_escolas = ["123", "12", "1"]

# Listas de alunos por ID da escola
nomes_alunos_1 = ["Luana Almeida", "Ruan Gonsalvez", "Deftoneron Scrobblers da Silva", "Maria Raimunda"]
nomes_alunos_12 = ["Sávio Cunha", "Bill Amostradinho do Lá Ele", "Mulch Lover", "Sister of the Loam"]
nomes_alunos_123 = ["Kiko Loureiro", "Alexi Laiho", "Dave Mustaine", "Alex Mikhail"]

# Dicionário com campos do aluno
campos_aluno = {
    'Nome': nome,
    'CPF': cpf,
    'Responsável': responsavel,
    'Foto': foto,
    'Id da escola': id_es
}

# Estilo para botão
st.markdown("""
<style>
    .stButton>button:hover {
        background-color: #FFD700;  /* Cor dourada */
        transform: scale(1.1);  /* Efeito de aumento */
        transition: 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

if st.button("Concluir"):
    if ver_preenchidos(campos_aluno):
        if id_es in ids_escolas:
            if id_es == "1" and nome in nomes_alunos_1:
                st.success("Concluído com sucesso!")
                sleep(0.5)
                st.write("Redirecionando para sala 1...")
                # st.experimental_rerun() ou st.switch_page("Pages/room1.py")
            elif id_es == "12" and nome in nomes_alunos_12:
                st.success("Concluído com sucesso!")
                sleep(0.5)
                st.write("Redirecionando para sala 12...")
                # st.switch_page("Pages/room12.py")
            elif id_es == "123" and nome in nomes_alunos_123:
                st.success("Concluído com sucesso!")
                sleep(0.5)
                st.write("Redirecionando para sala 123...")
                # st.switch_page("Pages/room123.py")
            else:
                st.error("Este aluno não pertence à escola cujo ID foi fornecido.")
        else:
            st.error("Este ID de escola não está cadastrado.")
    else:
        st.error("Por favor, preencha todos os campos.")
