from .settings import *
import os

WIBBLE2 = 'Wibble2'




# CSRF_TRUSTED_ORIGINS = ['https://*'] 
# TO-DO once deployed from VS code
CSRF_TRUSTED_ORIGINS = ['https://djangowebappx.azurewebsites.net', '*']

#add the next middleware for whitenoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#TO-DO add the static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
