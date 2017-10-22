import os

from .base import *

"""
Django settings file for you project.
"""

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ['DATABASE_NAME'],
    'USER': os.environ['USER'],
    'PASSWORD': os.environ['DATABASE_PASSWORD'],
    }
}

SECRET_KEY = os.environ['SECRET_KEY']