#!/usr/bin/env python3
"""
Script para executar a aplicação Flask
"""

import os
from app import app
from config import config

if __name__ == '__main__':
    # Determinar ambiente
    env = os.getenv('FLASK_ENV', 'development')
    
    # Aplicar configuração
    app.config.from_object(config.get(env, config['default']))
    
    # Configurações de execução
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    debug = env == 'development'
    
    print(f"🚀 Iniciando aplicação em modo {env}")
    print(f"📍 Servidor: http://{host}:{port}")
    
    # Executar aplicação
    app.run(
        host=host,
        port=port,
        debug=debug,
        threaded=True
    )