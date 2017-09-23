#!/usr/bin/env python
from setuptools import setup


with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='github-stars',
    version='0.0.1',
    description='List repository stars and info through Gituhb v4 GraphQL API',
    long_description=long_description,
    url='https://github.com/hanksudo/github-stars',
    author='Hank Wang',
    author_email='drapho@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='stars github',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'githubstars=githubstars:main'
        ]
    }
)
