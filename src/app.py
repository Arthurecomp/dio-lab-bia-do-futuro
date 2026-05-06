import streamlit as st
from agente import perguntar_agente

st.set_page_config(page_title="FinBot", page_icon="💰")

st.title("FinBot - Assistente Financeiro Inteligente")

st.write("Pergunte sobre seus gastos, investimentos ou metas financeiras.")

# Input do usuário
user_input = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    if user_input:
        with st.spinner("Analisando suas finanças..."):
            resposta = perguntar_agente(user_input)
        st.success(resposta)
    else:
        st.warning("Digite uma pergunta antes de enviar.")