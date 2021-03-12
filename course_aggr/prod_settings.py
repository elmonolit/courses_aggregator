from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'uaiv!g_kqasf+5kerai0hdfhsdghasf*8ojc_h%z&*-26w3q=u_hn_s8vd$j!99a'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'courses',
        'USER': 'admin',
        'PASSWORD': ' ',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static_dev'),]
STATIC_ROOT = os.path.join(BASE_DIR,'static')
