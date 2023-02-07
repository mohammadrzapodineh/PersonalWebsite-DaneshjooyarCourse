import os.path
from pathlib import Path
from django.contrib import messages
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'test'
DEBUG = True

# ALLOWED_HOSTS = ['localhost', '127.0.0.1'] For Debug False Or Deploy Mod
ALLOWED_HOSTS = [] # for Debug True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    # 'Home'
    'Home.apps.HomeConfig',
    'Sliders.apps.SlidersConfig',
    'Resume.apps.ResumeConfig',
    'ContactUs.apps.ContactusConfig',
    'SiteSetting.apps.SitesettingConfig',
    'Blog.apps.BlogConfig',
    'Comments.apps.CommentsConfig',
    # Other apps
    'ckeditor',
    'ckeditor_uploader',
    'widget_tweaks',
    'captcha',
    'jalali_date',
    'sorl.thumbnail',
    'taggit'
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

ROOT_URLCONF = 'PersonalWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'SiteSetting.context_processors.setting_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'PersonalWebsite.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



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


LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'assets'
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')
MEDIA_ROOT = os.path.join(BASE_DIR, '/media')
MEDIA_URL = '/media/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CkEditor Configs
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
    'comment_config': {
        'toolbar': 'Basic'
    }
}

# Recaptcha config
RECAPTCHA_PUBLIC_KEY = '6LcK0xkhAAAAANXlIz5lkQqHSTWLIAeqQyNdDyS7' # Site Key - > Google Admin
RECAPTCHA_PRIVATE_KEY = '6LcK0xkhAAAAAL29P07xOq523-QWhW12PP4c2BRe' # Secret Key Google Admin

MESSAGE_TAGS = {
    messages.SUCCESS: 'success',
    messages.ERROR:'danger',
    messages.INFO:'warning',
    messages.DEBUG: 'secondary'
}


SITE_ID = 1