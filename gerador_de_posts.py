import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os

# ======= coloque sua chave aqui =========
OPENAI_KEY = os.getenv("API_KEY")

# ========================================

chat = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-4o",
    openai_api_key=OPENAI_KEY
)

st.title("Post-Pronto 🚀")
conteudo  = st.text_input("Conteúdo")
publico  = st.text_input("Público-alvo")
tom      = st.selectbox("Tom de voz", ["Amigável", "Profissional", "Urgente", "Divertido"])

template = """
Você é um copywriter especialista. Gere:
1) Um carrossel de instagram. Me devolva uma resposta em Markdown, separando os slides do carrossel muito bem. 
2) Uma descrição ótima.
conteudo: {conteudo}
Público-alvo: {publico}
Tom de voz: {tom}
"""
prompt = PromptTemplate.from_template(template)

if st.button("Gerar"):
    resposta = chat.invoke(prompt.format(conteudo=conteudo, publico=publico, tom=tom))
    st.subheader("Carrossel Instagram")
    st.write(resposta.content)
