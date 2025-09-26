from flask import Flask
from .config import config_by_name # Importa o dicionário de configurações

def create_app(config_name):
    """
    Função 'fábrica' para criar e configurar a aplicação Flask.
    """
    app = Flask(__name__)
    
    # Carrega as configurações do objeto importado
    app.config.from_object(config_by_name[config_name])
    
    # Aqui, futuramente, iremos inicializar extensões como o banco de dados,
    # registrar as rotas (blueprints), etc.
    
    @app.route("/health")
    def health_check():
        """Rota de exemplo para verificar se a API está no ar."""
        return "API is running!"
        
    return app