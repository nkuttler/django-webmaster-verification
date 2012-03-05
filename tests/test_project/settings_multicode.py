import sys

from django.utils.importlib import import_module


# Import default settings
settings_default = import_module('test_project.settings')
settings_multicode = sys.modules[__name__]
for key in dir(settings_default):
    if not key.startswith('__'):
        setattr(settings_multicode, key, getattr(settings_default, key))

# And override what we want
WEBMASTER_VERIFICATION = {
    'google': (
        'ffffffffffffffff',
        'aaaaaaaaaaaaaaaa',
    ),
    'bing': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
    'majestic': (
        'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    ),
}
