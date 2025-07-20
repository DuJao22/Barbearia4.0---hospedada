import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

class Config:
    """Configurações base da aplicação"""
    
    # Configurações básicas
    SECRET_KEY = os.getenv('SECRET_KEY', 'chave_secreta_barbearia_2025')
    
    # Configurações do banco de dados
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlitecloud://chtue0yuhk.g1.sqlite.cloud:8860/barbearia.db?apikey=oa2q9I4Zp3I2L8e15StCNLZPgGH8N2Yd89NB7ofW6Lo')
    
    # Configurações de upload
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'static/uploads')
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 16777216))  # 16MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    # Configurações de ambiente
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = FLASK_ENV == 'development'

class DevelopmentConfig(Config):
    """Configurações para desenvolvimento"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurações para produção"""
    DEBUG = False

# Configuração baseada no ambiente
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}