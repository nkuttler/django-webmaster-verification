import os

TESTS_DIR = os.path.dirname(os.getcwd())

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}

ROOT_URLCONF = 'test_project.urls'

INSTALLED_APPS = (
    'webmaster_verification',
)

TEMPLATE_DIRS = (
    TESTS_DIR + '/test_project/templates/',
)

WEBMASTER_VERIFICATION = {
    'google': 'ffffffffffffffff',
    'bing': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
    'majestic': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
    'yandex': 'f0f0f0f0f0f0f0f0',
}

SECRET_KEY = 'CHANGE_THIS_TO_SOMETHING_UNIQUE_AND_SECURE'
