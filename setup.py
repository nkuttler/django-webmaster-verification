from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name = "webmaster_verification",
    version = "0.1",
    author = "nkuttler",
    author_email = "python@nicolaskuttler.com",
    description = "Webmaster tools verification for Django",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://github.com/nkuttler/django-webmaster-verification",
    packages=find_packages(),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)
