import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:oa2exWako@localhost/redo'
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

    SQLALCHEMY_DATABASE_URI= 'postgresql://xssplxlupcgmcp:ebf9a96b5c127f10fad32ad4a769d627ef62791d4e86ad382775f51899027dd8@ec2-107-22-238-112.compute-1.amazonaws.com:5432/d51krre9nc5vq5'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:oa2exWako@localhost/redo'

    DEBUG = True

config_options= {
    'development':DevConfig,
    'production':ProdConfig
}