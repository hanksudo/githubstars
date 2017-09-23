Github Stars
============

.. image:: https://img.shields.io/pypi/v/githubstars.svg
    :target: https://pypi.python.org/pypi/githubstars

.. image:: https://img.shields.io/pypi/l/githubstars.svg
    :target: https://pypi.python.org/pypi/githubstars

.. image:: https://img.shields.io/pypi/pyversions/githubstars.svg
    :target: https://pypi.python.org/pypi/githubstars


List repository stars and info through Gituhb v4 GraphQL API

.. code-block:: bash

    $ githubstars --lang python
    ⭐ 38867 awesome-python
    ⭐ 31578 httpie
    ⭐ 30981 thefuck
    ⭐ 29831 flask
    ⭐ 29402 youtube-dl

    $ githubstars django --lang python --count 5 --url --desc
    ⭐ 28394 django (https://github.com/django/django)
    - The Web framework for perfectionists with deadlines.

    ⭐ 13937 sentry (https://github.com/getsentry/sentry)
    - Sentry is a cross-platform crash reporting and aggregation platform.

    ⭐ 8685 django-rest-framework (https://github.com/encode/django-rest-framework)
    - Web APIs for Django.

    ⭐ 5196 django-cms (https://github.com/divio/django-cms)
    - The easy-to-use and developer-friendly CMS

    ⭐ 4931 Zappa (https://github.com/Miserlou/Zappa)
    - Serverless Python Web Services

Installation
============
.. code-block:: bash

    $ pip install githubstars
    $ export GITHUB_API_TOKEN="<your token here>"

Since Github require OAuth token to access GraphQL server, you must set personal access token first.

Refer: `Authenticating with GraphQL <https://developer.github.com/v4/guides/forming-calls/#authenticating-with-graphql>`_  and `Creating a personal access token for the command line <https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/>`_ 

Usage
=====
.. code-block:: bash
    
    $ githubstars -h
    usage: githubstars [-h] [--lang] [--count] [--desc] [--url] [--verbose]
                       [--version]
                       [repo]

    List repository stars and info through Gituhb v4 GraphQL API

    positional arguments:
    repo        repository name to search

    optional arguments:
    -h, --help  show this help message and exit
    --lang      search based on language
    --count     number of repositories to show
    --desc      show repo description
    --url       show repo url
    --verbose   show request detail
    --version   show version

Reference
=========

#. `GitHub API | GitHub Developer Guide <https://developer.github.com/v4/>`__
#. `GraphQL API Explorer | GitHub Developer Guide <https://developer.github.com/v4/explorer/>`__
#. `Creating a personal access token for the command line - User Documentation <https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/>`__
#. `Searching repositories - User Documentation <https://help.github.com/articles/searching-repositories/#search-based-on-the-main-language-of-a-repository>`__
