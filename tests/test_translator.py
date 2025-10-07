# Arquivo de exemplo para testes
import unittest
from utils.utils import extract_article_text
from article_translator.translator import ArticleTranslator

class TestArticleTranslator(unittest.TestCase):
    def test_extract_article_text(self):
        url = "https://dev.to/alifar/automating-text-to-video-pipelines-with-sora-2-and-n8n-lh0"
        text = extract_article_text(url)
        self.assertIsInstance(text, str)
        self.assertTrue(len(text) > 0)

    def test_translate_article(self):
        translator = ArticleTranslator()
        result = translator.translate_article("Hello world!", "português")
        self.assertIn("Olá", result)

if __name__ == "__main__":
    unittest.main()
