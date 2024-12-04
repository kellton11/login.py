import streamlit as st
import base64
import streamlit as st

# Injetar CSS para a imagem de fundo-pedro
st.markdown(
    """
    <style>
    body {
        background-image: url("https://i.pinimg.com/736x/fb/6e/a2/fb6ea2473d772ddd1410ea8aafdf87c3.jpg"); /* Substitua pelo URL da sua imagem */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Ajustando a opacidade do conteúdo */
    .main {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Conteúdo do Streamlit
st.title("Exemplo com Imagem de Fundo")
st.write("Esta aplicação tem uma imagem de fundo estilizada com CSS.")

# Um pequeno formulário para exemplo
name = st.text_input("Digite seu nome:")
if name:
    st.write(f"Olá, {name}!")

#informaçoes-pedro

st.title("Bem-Vindo, conheça um pouco sobre nós")

# Usando Markdown com CSS para personalizar o título
st.markdown("""
    <style>
        .big-title {
            font-size: 60px;
            font-weight: bold;
        }
    </style>
    <h1 class="big-title">Este é um título grande!</h1>
""", unsafe_allow_html=True)

#mais informac-çoes

st.write("Nosso objetivo")
st.text("nosso objetivo é oferecer segurança durante o ato de votação ")

#colocar um ponto de interrogaçao nesse "quem somos", nao estou conseguindo.

st.write("Quem somos")
st.text("Nossa empresa busca prestar segurança e confiacom aos nossos usuarios, com eficiência. visando a melhor experiência dos clientes ao votar em seus candidatos a liderança da gestão escolar.")

st.write("Vote consciente")

# CSS para criar cards
st.markdown("""
    <style>
    .card {
        background-color: #f9f9f9;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin-bottom: 20px;
    }

    .card h3 {
        color: #FF6347;
    }

    .card p {
        color: #555555;
    }
    </style>
""", unsafe_allow_html=True)

# Exemplo de Card
st.markdown('<div class="card"><h3>Card 1</h3><p>Conteúdo do card 1. Você pode usar isso para informações, imagens, etc.</p></div>', unsafe_allow_html=True)
st.markdown('<div class="card"><h3>Card 2</h3><p>Conteúdo do card 2. Exemplo de outro card com estilo.</p></div>', unsafe_allow_html=True)
 
#funçao para o usuario dizer de qual sala pertence

import streamlit as st

# CSS customizado para estilizar os botões
st.markdown(
    """
    <style>
    .course-button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }

    .course-button:hover {
        background-color: #45a049;
    }

    .course-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.title("Escolha o seu Curso")

# Lista de cursos disponíveis
courses = ["Desenvolvimento de Sistemas", "Administração", "Energias Renováveis", "Agrongócio", "Estética", "Contabilidade"]

# Criação dos botões de seleção para cada curso
st.markdown('<div class="course-container">', unsafe_allow_html=True)

for course in courses:
    if st.button(course, key=course, use_container_width=False):
        st.success(f"Você selecionou o curso: {course}")

st.markdown('</div>', unsafe_allow_html=True)


#checkbox

import streamlit as st

# CSS para customizar checkboxes
st.markdown("""
    <style>
    .stCheckbox input[type="checkbox"] {
        accent-color: #FF6347;
    }

    .stRadio input[type="radio"] {
        accent-color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Checkbox e Radio Buttons
if st.checkbox('Aceito os termos e condições'):
    st.write('Você aceitou os termos.')

option = st.radio('Gremio estudantil ou lideres de sala:', ['Gremio estudantil', 'Lideres de sala'])
st.write(f'Você escolheu: {option}')
 
if option == "Gremio estudantil":
    st.header("Você decidiu votar para os lideres do gremio")
    st.write("room1")
else:
    st.header("Você decidiu votar para a liderança de sala")
    st.write(f"seu curso é:{option} ")   

def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str

def cadastro():
    background_image_path = "img/novo.jpeg"  # Certifique-se de que o caminho está correto
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

# Chamada da função para carregar o fundo
cadastro()

def ver_preenchidos(campos):
    return all(campos.values())
