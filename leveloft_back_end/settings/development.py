from .settings import *
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'leveloft_db',
        'USER': 'leveloft_db_user',
        'PASSWORD': 'Qazwsx1@',
        'HOST': 'localhost',
        # 'PORT': 5433
    }
}