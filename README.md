# article_translator
Translator for articles from url

<div align="center">
	<img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python">
	<img src="https://img.shields.io/badge/OpenAI-Azure-blueviolet?logo=openai" alt="Azure OpenAI">
	<img src="https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-green?logo=beautifulsoup" alt="BeautifulSoup">
</div>

# 📰 Article Translator

> Tradutor automático de artigos extraídos de URLs, utilizando Azure OpenAI e BeautifulSoup.

---

## 🚀 Funcionalidades

- Extração de texto limpo de artigos online
- Tradução automática para qualquer idioma suportado
- Retorno em formato Markdown
- Estrutura modular e fácil de configurar

---

## 📦 Estrutura do Projeto

```bash
article_translator/
├── article_translator/
│   └── translator.py
├── config/
│   └── config.py
├── utils/
│   └── utils.py
├── main.py
├── README.md
└── tests/
```

---

## 🛠️ Instalação

```bash
git clone https://github.com/Abpereira/article_translator.git
cd article_translator
pip install -r requirements.txt
```

---

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto com suas credenciais:

```env
AZURE_ENDPOINT="<sua_url_azure_openai>"
API_KEY="<sua_api_key>"
API_VERSION="2024-02-15-preview"
DEPLOYMENT_NAME="gpt-4o-mini"
MAX_RETRIES=0
```

---

## 💡 Como Usar

```bash
python main.py
```

Você será solicitado a informar a URL do artigo e o idioma de destino.

---

## 🖼️ Exemplo Visual

<img src="https://user-images.githubusercontent.com/25181517/183911547-990692bc-8411-4c6a-8b74-6c0b3c3e5b8c.png" width="600"/>

---

## 🧪 Testes

Em breve!

---

## 📄 Licença

MIT
