#!/usr/bin/env python3
#
# tagedit <https://github.com/msikma/tagedit>
# © MIT license

"""
Installation script. To install for production, run:

    ./setup.py install

When developing, replace 'install' with 'develop'.
"""
from setuptools import setup, find_packages

setup(
    name='tagedit',
    version='1.0.0',
    description='Helper command line tool for running the MediaFile library',
    url='https://github.com/msikma/tagedit',
    author='Michiel Sikma',
    author_email='michiel@sikma.org',
    license='MIT',
    test_suite='tagedit.tests',
    packages=find_packages(),
    install_requires=[
        'mediafile >= 0.6.0, < 1.0.0'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9'
    ],
    entry_points={
        'console_scripts': [
            'tagedit=tagedit.cli.tagedit:main'
        ]
    },
    zip_safe=True
)
