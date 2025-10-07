# utils.py
# Funções utilitárias para o projeto
import requests
from bs4 import BeautifulSoup

def extract_article_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for script_or_style in soup(["script", "style"]):
            script_or_style.extract()
        text = soup.get_text(separator=' ')
        lines = (line.strip() for line in text.splitlines())
        parts = (phrase.strip() for line in lines for phrase in line.split("  "))
        clean_text = '\n'.join(part for part in parts if part)
        return clean_text
    else:
        print(f"Failed to retrieve the article. Status code: {response.status_code}")
        return None
