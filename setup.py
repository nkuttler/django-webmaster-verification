from setuptools import setup, find_packages


setup(
    name="django-webmaster-verification",
    version="0.4.3",
    packages=find_packages(),
    author="Nicolas Kuttler",
    author_email="pypi@kuttler.eu",
    description="Webmaster tools verification for Django",
    long_description=open("README.rst").read(),
    license="BSD",
    url="http://github.com/nkuttler/django-webmaster-verification",
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=["Django >= 3.0", ],
    zip_safe=True,
)
