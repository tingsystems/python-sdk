#!/usr/bin/python
# coding: utf-8

from setuptools import setup, find_packages

version = "1.0"
author = "Mercado Libre"

setup(
    name='',
    version=version,
    author=author,
    author_email='ayuda@mercadolibre.com.mx',
    url='https://github.com/mercadolibre/python-sdk',
    description='This is the official Python SDK for MercadoLibre Platform.',
    long_description=open('./README.txt', 'r').read(),
    download_url='https://github.com/mercadolibre/python-sdk',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(),
    install_requires=[
        'requests',
        'simplejson',
        'nose'
    ],
    license='MIT License',
    keywords='mercadolibre wrapper',
    include_package_data=True,
    zip_safe=True,
)
