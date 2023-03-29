"""
Django settings for power_building project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os  
from pathlib import Path
import dj_database_url  
import django_on_heroku  
from decouple import (
    config,
)  
# from dotenv import load_dotenv
# load_dotenv()

import environ
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "fitness",
    "members",
    "social",
    # third party 
    "django_extensions",
    'infscroll',
    "crispy_forms",  
    "ckeditor",  
    "ckeditor_uploader",  
    "rest_framework",
    "whitenoise.runserver_nostatic",
    "debug_toolbar",
    
    
    #aws
    'storages',
    
]

# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  
]

ROOT_URLCONF = "power_building.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": [],
        "DIRS": [
            os.path.join(BASE_DIR, "templates")
        ], 
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "power_building.wsgi.application"
AUTH_USER_MODEL = "members.User"  

''' added for cripsy forms its also accessing bootstrap4 '''
CRISPY_TEMPLATE_PACK = (
    "bootstrap4"  
)

''' for ckeditor and django ckeditor 5 '''
DJANGO_WYSIWYG_FLAVOR = "ckeditor"
CKEDITOR_JQUERY_URL = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"

'''Only who upload image see it '''
CKEDITOR_RESTRICT_BY_USER = True   
CKEDITOR_UPLOAD_PATH = "uploads/"

'''Shows directory of image in the server'''
CKEDITOR_BROWSE_SHOW_DIRS = True 

'''Arranges image in terms of date uploaded'''
CKEDITOR_RESTRICT_BY_DATE = True  
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    "default": {"toolbar": None, "extraPlugins": "codesnippet",},
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


'''
    required for the dj_databse_url module
    https://pypi.org/project/django-database-url/
'''
db_from_env = dj_database_url.config(
    conn_max_age=500
)  
DATABASES["default"].update(
    db_from_env
)  


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

#amazons3
# AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY_ID = env("AWS_SECRET_ACCESS_KEY_ID")
# AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_DEFAULT_ACL = 'public-read'
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400'
# }
# AWS_LOCATION = 'static'
# AWS_QUERYSTRING_AUTH = False
# AWS_HEADERS = {
#     'Access-Control-Allow-Origin': '*'
# }
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



'''media files'''
MEDIA_URL = "/media/"  
MEDIA_ROOT = os.path.join(
    BASE_DIR, "media"
)  

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = "static/"
STATIC_URL = "/static/"  
STATICFILES_DIRS = [  
    os.path.join(
        BASE_DIR, "static"
    ),  
]
STATIC_ROOT = os.path.join(
    BASE_DIR, "staticfiles"
)  
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  


'''
    login and logout returns user to homepage
    https://docs.djangoproject.com/en/4.0/topics/auth/customizing/
'''
LOGIN_REDIRECT_URL = "home"  
LOGOUT_REDIRECT_URL = "home"  

'''email hidden variables'''
# EMAIL_BACKEND = str(os.getenv("EMAIL_BACKEND"))
# EMAIL_USE_TLS = str(os.getenv("EMAIL_USE_TLS"))
# EMAIL_HOST = str(os.getenv("EMAIL_HOST"))
# EMAIL_HOST_USER = str(os.getenv("EMAIL_HOST_USER"))
# DEFAULT_FROM_EMAIL = str(os.getenv("DEFAULT_FROM_EMAIL"))
# EMAIL_HOST_PASSWORD = str(os.getenv("EMAIL_HOST_PASSWORD"))
# EMAIL_PORT = str(os.getenv("EMAIL_PORT"))

EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

'''
    Default primary key field type
    https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
'''
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    # ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',   # added from DRF JWT
        # 'rest_framework.authentication.BasicAuthentication'
    ],
    "DEFAULT_PERMISSIONS_CLASSES": [
        # 'rest_framework.permissions.AllowAny',
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
}

'''required for django heroku'''
django_on_heroku.settings(locals())  
