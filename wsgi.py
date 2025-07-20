"""
WSGI config para produção
"""

import os
from app import app
from config import config

# Configurar para produção
env = os.getenv('FLASK_ENV', 'production')
app.config.from_object(config.get(env, config['production']))

if __name__ == "__main__":
    app.run()