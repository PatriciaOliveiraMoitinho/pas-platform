import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Caminho base do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Configuração base, da qual as outras herdam."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'uma_chave_secreta_padrao_muito_dificil')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Configuração para o ambiente de desenvolvimento."""
    DEBUG = True
    # Se a DATABASE_URL não estiver definida, usa SQLite como fallback.
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '..', 'app-dev.db')

class TestingConfig(Config):
    """Configuração para o ambiente de testes."""
    DEBUG = True
    TESTING = True
    # Usa um banco de dados em memória para os testes.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(Config):
    """Configuração para o ambiente de produção."""
    DEBUG = False
    # Em produção, a DATABASE_URL deve ser definida.
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


# Dicionário para mapear nomes de configurações para suas respectivas classes.
config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY