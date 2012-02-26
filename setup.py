try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = "django-webmaster-verification",
    version = "0.1.3",
    author = "Nicolas Kuttler",
    author_email = "pypi@nicolaskuttler.com",
    description = "Webmaster tools verification for Django",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://github.com/nkuttler/django-webmaster-verification",
    packages = ['webmaster_verification'],
    include_package_data = True,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    install_requires = [
        "Django >= 1.3",
    ],
    zip_safe = True,
)
