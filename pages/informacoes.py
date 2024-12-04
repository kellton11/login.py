import streamlit as st

#titulo\ cabeçario

st.title("Sobre nòs")


#informaçoes 

st.write("Nosso objetivo")
st.text("Nosso objetivo é oferecer segurança durante as eleições escolares")

#coloquem um ponto de interrogaçao nesse "quem somos"

st.write("Quem somos")
st.text("Nossa empresa busca prestar segurança e confiança aos nossos usuarios, com eficiência. Visando a melhor experiência dos clientes ao votar.")

st.write("Vote consciente")

#css para criar cards, falta terminar!

st.markdown(""" 
          <styles>
        .card {
            background-color: #f9f9f9;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1)
            padding: 20px;
            margin-bottom: 20px;
        } 

        .card h3 {
            col 20px:
            }   
            
            """)

#card teste

st.markdown("""
         .card:hover 
            .card-background {
            transform: scale(1.15) translatez(0);
            background-size: 300px;
        }
        .card-grid:hover >.card:not(:hover){
            transform: scale(.9);
        }

        .card-grid:hover >  .card:not(:hover) .card-background,
            .card-grid:hover > .card:not(:hover)  .card-category {
            filter: brightness(0.5) saturate (0) contrast (1.2) blur (20px); 
            }
            
            """)

