import os
class Config:
    API_BASE_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SOURCE_API_BASE_URL='https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    API_BASE='https://newsapi.org/v2/everything?apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    '''
    General configuration parent class
    '''
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}

