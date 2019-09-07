import os
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'some string that is not hard'
    WTF_CSRF_TIME_LIMIT = None
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True

class TestingConfig(Config):
    WTF_CSRF_ENABLED = False
    TESTING=True

class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
