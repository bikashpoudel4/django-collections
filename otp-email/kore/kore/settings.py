from pathlib import Path
import os
import datetime


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-ed--skbhl=@3$s!yz2604$du6kjg=9kqhtxw4wc&gci83*2b_c'
SECRET_KEY = 'z3t)aj$23sulke&@e=t67=3x^pznl_nza=rfgj&0x3-t6&9md1s69xgw$yd!rt!gqd0lt+%t&a386@5#)9t2q3hnexet9*^b59h2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

# ALLOWED_HOSTS = ['85.214.238.109', 'localhost']
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
     # THIRD PARTY LIB
    'rest_framework', # djangorestframework
    'rest_framework_jwt', # djangorestframework-jwt
    'corsheaders', # django-cors-headers
    'drf_yasg', # drf-yasg
    
    # OWN APPS IN SYSTEM
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',## Cache First middleware django    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware', # django-cors-headers MIDDLEWARE must be included
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',## Cache Last middleware django
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'kore.wsgi.application'


###############--DB Manuals--#######################

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

## settings for MySql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'licArrtsm', #DB NAME
#         'USER': 'root',
#         'PASSWORD': '', #password
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'OPTIONS': {
#             'sql_mode': 'traditional',
#         }
#     }
# }

# # Settings for Postgres
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'fc',
#         'USER': 'fc',
#         'PASSWORD': 'Admin@123',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
###############--DB Manuals--#######################

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


####################################--MANUAL--##########################################

## Settings for Static Files and Media Files
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

## Scoping the user Authentication model in an app
AUTH_USER_MODEL = 'accounts.UserProfiile'

## Rest Framework Settings
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        # "rest_framework.permissions.IsAuthenticated",
        # "rest_framework.permissions.IsAdminUser",
        # "rest_framework.permissions.IsAuthenticatedOrReadOnly",
        "rest_framework.permissions.AllowAny",
        ),

    ## Authentication Classes
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

SESSION_COOKIE_SECURE = True
## To login via browserable api
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # 'accounts.backends.MyAuthBackend',
)

## For email host settings
# #it can be written in separate Files and use os environ

# for sending email to user or enabling email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
SITE_NAME = "Bikash Poudel Email"
# # # HOST EMAIL Settings [SMTP]
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
# # ##Use your host email and password
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# # HOST EMAIL Settings [SMTP]
# ##Use your host email and password
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
# EMAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')



## settings for djangorestframework-jwt
## JSONWebToken Settings
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',
    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',
    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',
    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    # Time for expiration of token
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

## CORS settings for CROSS ORIGIN RESOURCE SHARING
## Interaction between frontend framework and backend framework
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
   'http://192.168.0.1:4200',
)
CORS_ORIGIN_REGEX_WHITELIST = (
   'http://localhost:4200',
)
CORS_ALLOW_HEADERS = (
   'accept',
   'accept-encoding',
   'authorization',
   'content-type',
   'dnt',
   'origin',
   'user-agent',
   'x-csrftoken',
   'x-requested-with',
   'cache-control',
   'year',
)

## FOR TRY
# ##CORS ---- for choosing settings 
# CORS_ORIGIN_ALLOW_ALL=True
# CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOW_METHODS = (
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# )

# CORS_ALLOW_HEADERS = (
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
#     'X-API-TOKEN'
# )

## EXTRA 
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

####################################--MANUAL--##########################################