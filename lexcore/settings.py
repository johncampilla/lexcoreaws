"""
Django settings for lexcore project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d+m^^4+0bqm$sv7==)@h6r5s8iad94oim+cn3_o74)dw37ez0s'

# SECURITY WARNING: don't run with debug turned on in production!


DEBUG =True
# DEBUG = False

#ALLOWED_HOSTS = [".awsapprunner.com"]
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
#    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'emailportal',
    'activity',
    'casefolder',
    'client',
    'dashboard',
    'duecode_settings',
    'invoice',
    'matter',
    'reference_lookup',
    'users',
    'taskcode_settings',
    'userprofile',
    'docutemplates',
    # 3rd Party
    'django_countries',
    'chatter',

]

LOGIN_URL = '/login'

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lexcore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"lexcore/templates"],
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

WSGI_APPLICATION = 'lexcore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#==============My Postgresql in local ==================
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'lexcoredb',
#         'USER': 'postgres',
#         'PASSWORD':'640515john',
#         'HOST':'localhost',
#         'PORT':'5432',
#     }
#  }

#========================================================

#==================For Cloud Database======================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lexcoreDB',
        'USER': 'lexlinkuser',
        'PASSWORD': 'lexlinkuserjohn',
        'HOST': 'lexcoredb.cfms4k8s6k1z.ap-southeast-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
#============================================================================



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "lexcore/static"),)

MEDIA_ROOT = BASE_DIR/ 'media'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AWS_ACCESS_KEY_ID = 'AKIAUW6XQROOL5YCJVOY'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'lexcorebucket'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'ap-southeast-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.Emailbackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "LEXTRIM"


# EMAIL_USE_SSL = False
COMPANY_NAME = "SYCIP SALAZAR HERNANDEZ & GATMAITAN"