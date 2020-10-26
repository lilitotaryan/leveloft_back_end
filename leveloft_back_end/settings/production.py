from .settings import *
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'api.leveloft.am']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'megajack_leveloft_db',
        'USER': 'megajack_leveloft_db_user',
        'PASSWORD': 'csg%tarcad$hA',
        'HOST': 'localhost',
        # 'PORT': 5433
    }
}


HTTP_X_API_KEY = "6b551c62427b96ced354ad375fa09c09e705c3fa38ba27465a7469b9faed3acceccfea295a935cfae03f990d7188397b8b57518f79ff43383d93b4d28f16eecc"