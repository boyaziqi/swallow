import os

os.environ.setdefault('app_env', 'development')
enviroment = os.environ.get('app_env')

if not enviroment:
    raise Exception("don't set enviroment 'app_env'")

SETTINGS_MODULE = 'config.base'
if enviroment == 'development':
    SETTINGS_MODULE = 'config.develop'
elif enviroment == 'production':
    SETTINGS_MODULE = 'config.product'
