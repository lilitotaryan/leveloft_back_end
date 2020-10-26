from .settings import *
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'da3a54d12932.ngrok.io']


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

HTTP_X_API_KEY = "f7f7f4cbb6240647581c7a0db222cb06e7272f5f6e19532d324b223585321ed00911a8bd84d4cf3d3f5fbcfea305765d912b21a3bf37f62d7b378cb73ce2f784"