import os
from app import create_app

# Obtém a configuração a ser usada a partir da variável de ambiente FLASK_ENV.
# Se a variável não estiver definida, usa 'development' como padrão.
config_name = os.getenv('FLASK_ENV', 'development')
app = create_app(config_name)

if __name__ == '__main__':
    # Inicia o servidor de desenvolvimento do Flask.
    # O debug=True faz com que o servidor reinicie automaticamente
    # quando detecta alterações no código.
    app.run(debug=True)