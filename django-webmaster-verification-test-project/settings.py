DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'webmaster_verification',
    'test_app',
)

WEBMASTER_VERIFICATION = {
    'google': 'ffffffffffffffff',
    'bing': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
    'majestic': 'ffffffffffffffffffffffffffffffff',
}
