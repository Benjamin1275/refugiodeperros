"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

#TO_DO Add the secret key
SECRET_KEY = 'd6k+u*n+-h=0nl!7u=7)o0c=0#k5&-r)-7%)()_6fueef^14#^'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

##TO-DO Add the ALLOWED HOST FROM THE APP NAME
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'dog_shelters.apps.DogSheltersConfig',
    'core.apps.CoreConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    "crispy_bootstrap5",
    'health_check',                             
    'health_check.db',
                          
]



JAZZMIN_UI_TWEAKS = {
    "theme": "simplex",
}


JAZZMIN_SETTINGS = {
    "site_title": "Admin",
    "site_header": "Admin",
    "welcome_sign": "Bienvenido a la administración de la aplicación",
    "topmenu_links": [],
    "usermenu_links": [],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth"],
    "custom_links": {},
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {},
    "language_chooser": False,
}


CRISPY_ALLOWED_TEMPLATE_PACKS = ['bootstrap5']
CRISPY_TEMPLATE_PACK = 'bootstrap5'

CSRF_USE_SESSIONS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                        BASE_DIR / 'templates', #Se agreggo BASE_DIR / 'templates' para que busque en la carpeta templates
                ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#TO-DO update db to use the postgresql / Azure and ElephantDb
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangodbbenja', #Nombre bd
        'HOST': 'djangoweb2024.postgres.database.azure.com', #Host bd
        'USER': 'benjadb',
        'PASSWORD': 'ProgramacionWeb#',
        'PORT': '5432', #Buscado en django postgresql
        'OPTIONS': {
            'sslmode': 'require', #Bd remota o en la nube se utiliza sslmode require
        },
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'core.CustomUser'  
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


# Variables de redirrecion de login y logout
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

