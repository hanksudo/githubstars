#!/usr/bin/env python
from setuptools import setup


with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='githubstars',
    version='0.0.4',
    description='List repository stars and info through Gituhb v4 GraphQL API',
    long_description=long_description,
    url='https://github.com/hanksudo/githubstars',
    author='Hank Wang',
    author_email='drapho@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='stars github graphql',
    py_modules=['githubstars'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'githubstars=githubstars:main'
        ]
    }
)
