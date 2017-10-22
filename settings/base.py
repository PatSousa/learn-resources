from settings.core import *

import json
from django.core.exceptions import ImproperlyConfigured

key = "secrets.json"
with open(key) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secret=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")

_db_name = get_secret("DB_NAME")
_db_host = get_secret("DB_HOST")
_db_password = get_secret("DB_PASSWORD")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': _db_name,
        'USER': _db_host,
        'PASSWORD': _db_password,
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}