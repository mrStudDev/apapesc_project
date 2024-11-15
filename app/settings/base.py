import os
from pathlib import Path
import environ

# Inicializa o django-environ
env = environ.Env()
environ.Env.read_env(os.path.join(Path(__file__).resolve().parent.parent, '.env'))

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = env("SECRET_KEY", default="chave-padrao-insegura")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'ckeditor',
    'ckeditor_uploader',
    'app_home',
    'app_manager',
    'app_associados',
    'app_documentos',
]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Middleware do allauth
    'allauth.account.middleware.AccountMiddleware',  # Linha faltante
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',  # Isso permite login tradicional
)



WSGI_APPLICATION = 'app.wsgi.application'

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = '/manager/dashboard/'  # Após login, redirecionar para a homepage
LOGOUT_REDIRECT_URL = '/'  # Após logout, redirecionar para a homepage
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Para debug (não envia e-mails reais)


CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"  # Certifique-se de ter o Pillow instalado para manipulação de imagem

# Configurações opcionais para personalizar o CKEditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Maximize'],
            {'name': 'clipboard', 'items': ['Undo', 'Redo']},
            {'name': 'styles', 'items': ['Format', 'Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat', 'TextColor', 'BGColor']},
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat', 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote',]}, # Adiciona estilos básicos
            {'name': 'paragraph', 'items': ['-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']}, # Aprimora opções de parágrafo
            {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak']}, # Adiciona opções de inserção
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']}, # Adiciona opções de links
            {'name': 'document', 'items': ['Source']}, # Adiciona botão para visualizar o código-fonte
            '/', # Adiciona uma separação visual entre as toolbars
            {'name': 'your_custom_toolbar', 'items': [ 'Preview', 'Templates']}, # Exemplo de toolbar customizada

        ],
        'height': 300,
        'width': '100%',
        'extraPlugins': ','.join(['uploadimage', 'image2', 'colorbutton']),
        'filebrowserUploadUrl': '/ckeditor/upload/',
        'removeButtons': '',
    },
}


