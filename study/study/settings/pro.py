from .base import *


DEBUG = False


ADMINS = (
    ('Zhang Wenzhi', 'luffybjdf@163.com'),
)


ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECURE_SSL_REDIRECT =False
CSRF_COOKIE_SECURE =False

