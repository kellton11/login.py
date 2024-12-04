import streamlit as st

st.button("SOFRENCIA")
st.markdown("""/* Contêiner Flex */
.container {
  display: flex;
  flex-direction: row; /* Alinha os itens horizontalmente */
  justify-content: space-between; /* Distribui os itens com espaçamento igual entre eles */
  align-items: center; /* Alinha os itens ao centro verticalmente */
  height: 200px; /* Define a altura do contêiner */
}

/* Itens Flexíveis */
.item {
  background-color: lightblue;
  padding: 10px;
  text-align: center;
  flex-grow: 1; /* Faz os itens crescerem igualmente */
  margin: 5px; /* Espaço entre os itens */
}
""")