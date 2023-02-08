import os
import json
from pathlib import Path
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

# Read settings.json
try:
    config_path = os.path.join(BASE_DIR, 'settings.json')
    config = json.load(open(config_path, "r", encoding="utf-8"))
except FileNotFoundError as e:
    print("[ERROR] Config file is not found.")
    raise e
except ValueError as e:
    print("[ERROR] Json file is invalid.")
    raise e

secret_key = config['SECRET_KEY']
email_host = config['EMAIL_HOST']
email_host_pass = config['EMAIL_HOST_PASS']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('GAE_APPLICATION', None):
    # 本番環境
    DEBUG = False
else:
    # 開発環境
    DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 

    'cafe_app.apps.CafeAppConfig', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cafe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'cafe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Settings of logger

LOGGING = {
    'version': 1,   # 1固定
    'disable_existing_loggers': False, 

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'], 
            'level': 'INFO', 
        }, 
        # cafe_appアプリケーションが利用するロガー
        'cafe_app': {
            'handlers': ['console'], 
            'level': 'DEBUG', 
        }, 
    }, 

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG', 
            'class': 'logging.StreamHandler', 
            'formatter': 'dev',
        }, 
    }, 

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s', 
                '[%(levelname)s]', 
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        }, 
    }
}

# settings of static file path

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'), 
)

# メッセージレベルに応じたタグ
MESSAGE_TAGS = {
    messages.ERROR: 'message-danger', 
    messages.WARNING: 'message-warning', 
    messages.SUCCESS: 'message-success', 
    messages.INFO: 'message-info', 
}

# メールの配信先の設定
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'    # [開発時用]コンソール上に内容を表示させる
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'       # [運用時用]

# メールサーバー設定
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = email_host
EMAIL_HOST_PASSWORD = email_host_pass
EMAIL_USE_TLS = True
