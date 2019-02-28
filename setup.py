#!/usr/bin/env python

from setuptools import setup, find_packages

import provider

setup(
    name='wml-django-oauth2-provider',
    version=provider.__version__,
    description='WMLabs fork of edx-django-oauth2-provider',
    long_description=open('README.rst').read(),
    author='Grant Viklund',
    author_email='grantv@whitemoondreams.com',
    url='https://github.com/WhiteMoonDreamsInc/django-oauth2-provider',
    packages=find_packages(exclude=('tests*',)),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires=">=3.6",
    install_requires=[
        'shortuuid>=0.4.3,<1.0.0', 
        'Django>=2.1'
    ],
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'dev': [],
        'test': [
            'coverage>=4.0.3,<5.0.0',
            'ddt>=1.0.1,<2.0.0',
            'django-nose>=1.4.3,<2.0.0',
            'mock>=1.3.0,<2.0.0',
        ],
        'prod': [],
        'build': [],
        'docs': [
            'coverage>=4.0.3,<5.0.0',
            'Sphinx==1.6.4'],
    }
)


