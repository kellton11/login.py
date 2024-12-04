import streamlit as st

st.title("aqui estão alguns Feedbacks")

st.markdown("🎉 Parabéns, esse site é o melhor! 🎉")

st.markdown("me passa muita confiança")

#your feedback

st.title("Formulário de Feedback")

feedback = st.text_area("Deixe seu feedback: ")

if st.button("Enviar"):
    if feedback:
        st.success("Obrigado pelo seu feedback!")
    else:
        st.warning("Por favor, insira seu feedback antes de enviar.")

