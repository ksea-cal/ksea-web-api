from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': 5432,
        'NAME': 'kseadev',
        'USER': 'kseaapiuser',
        'PASSWORD': 'welikeksea',
    }
}
