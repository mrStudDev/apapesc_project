# Production
from .base import *

DEBUG = False
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS_PROD", default=["34.123.22.119"])


ROOT_URLCONF = 'app.urls'  # Certifique-se de que está configurado


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME_PROD", default="apapesc_db"),
        'USER': env("DB_USER_PROD", default="postgres"),
        'PASSWORD': env("DB_PASSWORD_PROD", default="password"),
        'HOST': env("DB_HOST_PROD", default="db"),
        'PORT': '5432',
    }
}
