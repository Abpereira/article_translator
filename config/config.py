# config.py
# Configurações e variáveis de ambiente para o projeto
import os

AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT')
API_KEY = os.getenv('API_KEY')
API_VERSION = os.getenv('API_VERSION', '2024-02-15-preview')
DEPLOYMENT_NAME = os.getenv('DEPLOYMENT_NAME', 'gpt-4o-mini')
MAX_RETRIES = int(os.getenv('MAX_RETRIES', '0'))
