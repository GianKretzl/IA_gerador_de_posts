# IA Gerador de Posts para Instagram

Este projeto é um gerador de posts para Instagram utilizando IA, desenvolvido em Python com [Streamlit](https://streamlit.io/) e [LangChain](https://python.langchain.com/). Ele utiliza modelos da OpenAI para criar carrosséis e descrições otimizadas para o seu público-alvo, com diferentes tons de voz.

## Funcionalidades

- Geração automática de carrosséis para Instagram em Markdown, com separação clara dos slides.
- Criação de descrições otimizadas para o post.
- Personalização do conteúdo, público-alvo e tom de voz.
- Interface web simples e intuitiva via Streamlit.

## Como usar

### 1. Clone o repositório

```sh
git clone https://github.com/GianKretzl/IA_gerador_de_posts.git
cd IA_gerador_de_posts
```

### 2. Instale as dependências

Recomenda-se o uso de um ambiente virtual:

```sh
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -r requeriments.txt
```

### 3. Configure sua chave da OpenAI

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
API_KEY="sua_chave_openai_aqui"
```

> **Dica:** Um modelo de arquivo `.env` está disponível como `.env_model`.

### 4. Execute o aplicativo

```sh
streamlit run gerador_de_posts.py
```

Acesse o endereço exibido no terminal (geralmente http://localhost:8501).

## Estrutura do Projeto

```
.
├── .env
├── .env_model
├── .gitattributes
├── .gitignore
├── gerador_de_posts.py
├── requeriments.txt
```

- `gerador_de_posts.py`: Código principal do app.
- `.env`: Variáveis de ambiente (API_KEY).
- `requeriments.txt`: Dependências do projeto.

## Personalização

- **Modelos OpenAI:** O modelo padrão é o `gpt-4o`, mas você pode alterar para outro modelo suportado pela OpenAI.
- **Tons de voz:** Personalize a lista de tons de voz no campo `st.selectbox` conforme sua necessidade.

## Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [OpenAI API](https://platform.openai.com/docs/api-reference)

## Licença

Este projeto está sob a licença MIT.

---

Desenvolvido por Gian Kretzl (https://github.com/GianKretzl/).