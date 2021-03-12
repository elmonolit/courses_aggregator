from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'uaiv!g_kq+5kerai0*8ojc_h%z&*-26w3q=u_hn_s8vd$j!99a'

DEBUG = True

ALLOWED_HOSTS = []


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



STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static_dev'),]


