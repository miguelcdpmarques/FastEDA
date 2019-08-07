import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '6b8b945c32aa6fe82769bfce9f805326'
    CORS_HEADERS='Content-Type'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SEED_ADMIN_EMAIL = os.environ.get('SEED_ADMIN_EMAIL') or 'admin'
    SEED_ADMIN_PASSWORD = os.environ.get('SEED_ADMIN_PASSWORD') or 'password'
    SSL_REDIRECT = False
    API_KEY = os.environ.get('API_KEY')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
            'postgresql://postgres:password@localhost:5433/fasteda_dev'


config = {
    'development': DevelopmentConfig,
}