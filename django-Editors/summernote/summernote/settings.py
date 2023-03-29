import os
from pathlib import Path
import django_heroku
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h*87w)@=$+h3h#c4iyrx0$#!29wb(zr2q%*q*n$1&$%!ic)9--'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'content',
    'rest_framework',
     
    #  django-summernote
     'django_summernote', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # HEROKU MIDDLEWARE
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # HEROKU MIDDLEWARE
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'summernote.urls'

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

WSGI_APPLICATION = 'summernote.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# HEROKU MIDDLEWARE
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

django_heroku.settings(locals())
# HEROKU MIDDLEWARE

###################################SummerNote ConfigS###########################################################
# django-summernote
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

SUMMERNOTE_THEME = 'bs4'  # Show summernote with Bootstrap4

X_FRAME_OPTIONS = 'SAMEORIGIN'

SUMMERNOTE_CONFIG = { 
    
    # Using SummernoteWidget - iframe mode, default
    'iframe': True,

    'summernote' : {
        # Define height and width here
        # 'width': '85%',
        'width': '100%',
        # 'height': '720',
        
         # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'underline']],
            ['script', ['strikethrough', 'superscript', 'subscript']],
            ['paragraph style', ['ol', 'ul', 'paragraph']],
            ['font2', ['fontname', 'fontsize', 'fontsizeunit']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['hr', ['hr']],
            ['maxm', ['fullscreen']],
            ['code', ['codeview']],
            ['clear', ['forecolor', 'backcolor', 'clear', 'color']],
            ['height', ['height']],
            ['solve', ['undo', 'redo']],
            ['help', ['help']],
        ],
        
        # You can also add custom settings for external plugins
        'print': {
            'stylesheetUrl': '/some_static_folder/printable.css',
        },
        
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            # # You have to include theme file in 'css' or 'css_for_inplace' before using it.
            # 'theme': 'monokai',
        },
    },
    # Require users to be authenticated for uploading attachments.
    'attachment_require_authentication': True,
    
    # You can completely disable the attachment feature.
    'disable_attachment': False,
    
    # Set to `True` to return attachment paths in absolute URIs.
    'attachment_absolute_uri': False,
    
    # Lazy initialization
    # If you want to initialize summernote at the bottom of page, set this as True
    # and call `initSummernote()` on your page.
    'lazy': True,
    
    # # To use external plugins,
    # # Include them within `css` and `js`.
    # 'js': {
    #     '/some_static_folder/summernote-ext-print.js',
    #     '//somewhere_in_internet/summernote-plugin-name.js',
    # },
}
#############################################################################################

