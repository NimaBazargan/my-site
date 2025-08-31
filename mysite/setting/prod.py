from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#h*$4=w!c4x6#pxf5))%n2ivg0ci*d)p2m-ur86(^-_3sq8r_='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['nimrimah.ir','www.nimrimah.ir']

#INSTALLED_APPS = []

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nimrimah_Travel',
        'USER': 'nimrimah_nimrimah',
        'PASSWORD': 'userS2Com7',
        'HOST': 'localhost',  # Set to the MySQL server's host, e.g., 'localhost'
        'PORT': '3306',       # Set to the MySQL server's port, if different from the default (3306)
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'statics'
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True