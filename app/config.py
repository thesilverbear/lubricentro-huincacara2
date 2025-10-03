# CÓDIGO COMPLETO PARA REEMPLAZAR EN config.py

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-por-defecto'

    # --- INICIO DEL CÓDIGO IMPORTANTE ---
    
    # Configuración inteligente de la base de datos para Railway y Local
    if 'MYSQLHOST' in os.environ:
        # Estamos en producción (Railway), construimos la URL desde las piezas
        user = os.environ.get('MYSQLUSER')
        password = os.environ.get('MYSQLPASSWORD')
        host = os.environ.get('MYSQLHOST')
        port = os.environ.get('MYSQLPORT')
        database = os.environ.get('MYSQLDATABASE')
        SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    else:
        # Estamos en desarrollo (local), usamos la URL del archivo .env
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
        
    # --- FIN DEL CÓDIGO IMPORTANTE ---

    # Solución para el error 'Access Denied' en Railway
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 280}
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False