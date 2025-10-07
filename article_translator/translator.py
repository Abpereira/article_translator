# translator.py
from langchain_openai.chat_models.azure import AzureChatOpenAI
from config.config import AZURE_ENDPOINT, API_KEY, API_VERSION, DEPLOYMENT_NAME, MAX_RETRIES

class ArticleTranslator:
    def __init__(self):
        self.client = AzureChatOpenAI(
            azure_endpoint=AZURE_ENDPOINT,
            api_key=API_KEY,
            api_version=API_VERSION,
            deployment_name=DEPLOYMENT_NAME,
            max_retries=MAX_RETRIES
        )

    def translate_article(self, text, lang):
        messages = [
            ("system", "Você deverá atuar como um tradutor de textos"),
            ("user", f"Traduza o {text} para o idioma {lang} e traga o retorno em markdown")
        ]
        response = self.client.invoke(messages)
        return response.content
