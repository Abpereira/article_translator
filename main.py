# main.py
from utils.utils import extract_article_text
from article_translator.translator import ArticleTranslator

if __name__ == "__main__":
    url = input("Digite a URL do artigo: ")
    lang = input("Digite o idioma de destino: ")
    text = extract_article_text(url)
    if text:
        translator = ArticleTranslator()
        translated = translator.translate_article(text, lang)
        print("\nArtigo traduzido:\n")
        print(translated)
    else:
        print("Não foi possível extrair o texto do artigo.")
