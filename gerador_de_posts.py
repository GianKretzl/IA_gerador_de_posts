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

st.set_page_config(page_title="Gerador de Posts IA", page_icon="🚀", layout="centered")
st.title("🚀 Gerador de Carrossel para Instagram com IA")
st.markdown(
    """
    Crie carrosséis e descrições otimizadas para Instagram em segundos.<br>
    <small>Preencha os campos abaixo e clique em <b>Gerar</b>.</small>
    """, unsafe_allow_html=True
)

with st.form("formulario"):
    conteudo  = st.text_area("Conteúdo do post", placeholder="Sobre o que é o post?")
    publico  = st.text_input("Público-alvo", placeholder="Ex: Jovens empreendedores")
    tom      = st.selectbox("Tom de voz", ["Amigável", "Profissional", "Urgente", "Divertido"])
    gerar = st.form_submit_button("Gerar")

if gerar:
    if not conteudo or not publico:
        st.warning("Preencha todos os campos para gerar o post.")
    else:
        template = """
        Você é um copywriter especialista. Gere:
        1) Um carrossel de instagram. Me devolva uma resposta em Markdown, separando os slides do carrossel muito bem usando '---' entre eles.
        2) Uma descrição ótima para o post, separada do carrossel.
        conteudo: {conteudo}
        Público-alvo: {publico}
        Tom de voz: {tom}
        """
        prompt = PromptTemplate.from_template(template)
        with st.spinner("Gerando conteúdo..."):
            resposta = chat.invoke(prompt.format(conteudo=conteudo, publico=publico, tom=tom))
        # Separar carrossel e descrição
        partes = resposta.content.split("Descrição:")
        carrossel = partes[0].strip()
        descricao = partes[1].strip() if len(partes) > 1 else ""
        st.subheader("🖼️ Carrossel (Markdown)")
        st.markdown(carrossel)
        st.subheader("✍️ Descrição")
        st.code(descricao, language="markdown")
        st.success("Conteúdo gerado! Copie e use no seu Instagram.")
