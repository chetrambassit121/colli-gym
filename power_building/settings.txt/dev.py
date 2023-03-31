from .base import *
import dj_database_url  


SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

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