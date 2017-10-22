import os

from .base import *

"""
Django settings file for you project.
"""

DATABASE_URL = os.environ['DATABASE_URL']

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ['DATABASE_NAME'],
    'USER': os.environ['USER'],
    'PASSWORD': os.environ['PASSWORD'],
    }
}

SECRET_KEY = os.environ['SECRET_KEY']
