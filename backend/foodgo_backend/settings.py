from pathlib import Path 
 
BASE_DIR = Path(__file__).resolve().parent.parent 
 
 
SECRET_KEY = 'django-insecure-foodgo-development-key' 
 
DEBUG = True 
 
ALLOWED_HOSTS = ['*'] 
 
 
INSTALLED_APPS = [ 
 
    'django.contrib.admin', 
 
    'django.contrib.auth', 
 
    'django.contrib.contenttypes', 
 
    'django.contrib.sessions', 
 
    'django.contrib.messages', 
 
    'django.contrib.staticfiles', 
 
    'corsheaders', 
 
    'rest_framework', 
 
    'api.apps.ApiConfig', 
] 
 
 
MIDDLEWARE = [ 
 
    'django.middleware.security.SecurityMiddleware', 

    'whitenoise.middleware.WhiteNoiseMiddleware',
 
    'corsheaders.middleware.CorsMiddleware', 
 
    'django.contrib.sessions.middleware.SessionMiddleware', 
 
    'django.middleware.common.CommonMiddleware', 
 
    'django.middleware.csrf.CsrfViewMiddleware', 
 
    'django.contrib.auth.middleware.AuthenticationMiddleware', 
 
    'django.contrib.messages.middleware.MessageMiddleware', 
 
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
] 
 
 
ROOT_URLCONF = 'foodgo_backend.urls' 
 
 
TEMPLATES = [ 
 
    { 
        'BACKEND': 
            'django.template.backends.django.DjangoTemplates', 
 
        'DIRS': 
            [BASE_DIR / 'templates'], 
 
        'APP_DIRS': 
            True, 
 
        'OPTIONS': { 
 
            'context_processors': [ 
 
                'django.template.context_processors.request', 
 
                'django.contrib.auth.context_processors.auth', 
 
                'django.contrib.messages.context_processors.messages', 
 
            ], 
        }, 
    }, 
] 
 
 
WSGI_APPLICATION = 'foodgo_backend.wsgi.application' 
 
 
DATABASES = { 
 
    'default': { 
 
        'ENGINE': 
            'django.db.backends.sqlite3', 
 
        'NAME': 
            BASE_DIR / 'db.sqlite3', 
    } 
} 
 
 
AUTH_PASSWORD_VALIDATORS = [ 
 
    { 
        'NAME': 
            'django.contrib.auth.password_validation.' 
            'UserAttributeSimilarityValidator', 
    }, 
 
    { 
        'NAME': 
            'django.contrib.auth.password_validation.' 
            'MinimumLengthValidator', 
    }, 
 
    { 
        'NAME': 
            'django.contrib.auth.password_validation.' 
            'CommonPasswordValidator', 
    }, 
 
    { 
        'NAME': 
            'django.contrib.auth.password_validation.' 
            'NumericPasswordValidator', 
    }, 
] 
 
 
LANGUAGE_CODE = 'en-us' 
 
TIME_ZONE = 'Asia/Kolkata' 
 
USE_I18N = True 
 
USE_TZ = True 
 
 
STATIC_URL = 'static/' 
 
STATICFILES_DIRS = [ 
    BASE_DIR / 'static', 
] 
 
STATIC_ROOT = BASE_DIR / 'staticfiles' 


STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
 
 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' 
 
 
CORS_ALLOW_ALL_ORIGINS = True 
 
 
TWO_FACTOR_API_KEY = "PASTE_YOUR_2FACTOR_API_KEY_HERE"