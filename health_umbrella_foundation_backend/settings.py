"""
Django settings for health_umbrella_foundation_backend project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG")

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "material",
    "material.admin",
    # "django.contrib.admin",  #commented to add a new theme
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",  # added to interact with AWS S3
    "home",
    "footer",
    "disease",
    "ejournal",
    "feedback",
    "pathy",
    "analytics"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "health_umbrella_foundation_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "health_umbrella_foundation_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }

    # AWS RDS connection settings
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": config("DATABASE_NAME"),
    #     "USER": config("DATABASE_USER"),
    #     "PASSWORD": config("PASSWORD"),
    #     "HOST": config("HOST"),
    #     "PORT": config("PORT"),
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# AWS S3 settings
# AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_CUSTOM_DOMAIN = config("AWS_S3_CUSTOM_DOMAIN")
# AWS_DEFAULT_ACL = config("AWS_DEFAULT_ACL")
# AWS_S3_OBJECT_PARAMETERS = {"CacheControl": f"max-age={config('MAX_AGE')}"}
# AWS_LOCATION = config("AWS_LOCATION")
# AWS_QUERYSTRING_AUTH = config("AWS_QUERYSTRING_AUTH")
# AWS_HEADERS = {
#     "Access-Control-Allow-Origin": f"{config('ACCESS_CONTROL_ALLOW_ORIGIN')}",
# }
# AWS_S3_VERIFY = False
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"

# STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
# MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

# setting to run application with aws on server
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

# CORS header settings
# CORS_ORIGIN_ALLOW_ALL = config("CORS_ORIGIN_ALLOW_ALL")
# CORS_ALLOW_CREDENTIALS = config("CORS_ALLOW_CREDENTIALS")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# configurations of material admin
MATERIAL_ADMIN_SITE = {
    'HEADER':  _('Health Umbrella'),  # Admin site header
    'TITLE':  _('HUF'),  # Admin site title
    # 'FAVICON':  'path/to/favicon',  # Admin site favicon (path to static should be specified)
    # 'MAIN_BG_COLOR':  'color',  # Admin site main color, css color should be specified
    # 'MAIN_HOVER_COLOR':  'color',  # Admin site main hover color, css color should be specified
    # 'PROFILE_PICTURE':  'path/to/image',  # Admin site profile picture (path to static should be specified)
    # 'PROFILE_BG':  'path/to/image',  # Admin site profile background (path to static should be specified)
    # 'LOGIN_LOGO':  'path/to/image',  # Admin site logo on login page (path to static should be specified)
    # 'LOGOUT_BG':  'path/to/image',  # Admin site background on login/logout pages (path to static should be specified)
    # 'SHOW_THEMES':  True,  #  Show default admin themes button
    # 'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
    # 'NAVBAR_REVERSE': True,  # Hide side navbar by default
    # 'SHOW_COUNTS': True, # Show instances counts for each model
    # 'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
    #     'sites': 'send',
    # },
    # 'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
    #     'site': 'contact_mail',
    # }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'log_file': {
            'level': 'INFO',  # Set the desired logging level
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/application.log',  # Regular log file
        },
        'error_file': {
            'level': 'ERROR',  # Set the desired logging level
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/error.log',  # Error log file
        },
    },
    'loggers': {
        'file_log': {
            'handlers': ['log_file', 'error_file'],
            'level': 'DEBUG',  # Set the desired logging level
            'propagate': True,
        },
        # You can add more loggers for other components of your app
    },
}


