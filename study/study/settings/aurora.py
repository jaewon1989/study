from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':  'study-instance.cwzkrgtyhcji.ap-northeast-2.rds.amazonaws.com',
        'NAME': 'study',
        'USER': 'admin',
        'PASSWORD': 'emeldjroqkf!#%',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    }
}