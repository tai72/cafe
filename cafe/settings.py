import os
import json
import environ
from pathlib import Path
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

# Read .env file
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

secret_key = env('SECRET_KEY')
email_host = env('EMAIL_HOST')
email_host_pass = env('EMAIL_HOST_PASS')
db_user_dev = env('DB_USER_DEV')
db_password_dev = env('DB_PASSWORD_DEV')
instance_connection_name = env('INSTANCE_CONNECTION_NAME')
db_user = env('DB_USER')
db_password = env.str('DB_PASSWORD')
db_name = env.str('DB_NAME')

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
    'accounts.apps.AccountsConfig', 
    
    'django.contrib.sites', 
    'allauth', 
    'allauth.account', 
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

if os.environ.get('GAE_APPLICATION', None):
    # 本番環境（GCP）
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': db_name,
            'USER': db_user,
            'PASSWORD': db_password,
            'HOST': f'/cloudsql/{instance_connection_name}',
        }
    }
# else:
    # 開発環境（PostgreSQL）
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'cafe_app',
    #         'USER': db_user_dev,
    #         'PASSWORD': db_password_dev,
    #         'HOST': '',
    #         'PORT': '',
    #     }
    # }
else:
    # 開発環境（Cloud SQL）
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': db_name,
            'USER': db_user,
            'PASSWORD': db_password,
            'HOST': '127.0.0.1',
            'PORT': '3306', 
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

# 認証時にカスタムユーザーモデルを参照する
AUTH_USER_MODEL = 'accounts.CustomUser'

# django.contrib.sites用のサイト識別IDを設定
SITE_ID = 1

# 認証バックエンドの設定
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',   # 一般ユーザー用（メールアドレス認証）
    'django.contrib.auth.backends.ModelBackend',    # 管理サイト用（ユーザー名認証）
)

# 認証方式を「メールアドレス」に設定
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False    # ユーザー名は使用しない

# サインアップにメールアドレス確認を挟むように設定
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True

# ログイン / ログアウト後のリダイレクト先を設定
LOGIN_REDIRECT_URL = 'cafe_app:index'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

# 「ログアウト」を一回クリックしただけでログアウトできるように設定
ACCOUNT_LOGOUT_ON_GET = True

# django-allauthが送信するメールの件名に自動付与される接頭辞を空にする設定
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

# デフォルトのメール送信元の設定
DEFAULT_FROM_EMAIL = email_host

# 開発環境におけるメディアファイルの配置場所（「media/」はGithub管理する必要なし）
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 画像を配信するURLのホスト名以下を指定
# 例えば「hoge.png」なら、'https://<ホスト名>/media/hoge.png'で配信される
MEDIA_URL = '/media/'
