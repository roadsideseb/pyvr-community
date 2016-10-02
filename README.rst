Manage the Python Community in Vancouver
===============================


.. image:: https://travis-ci.com//community.svg
    :target: https://travis-ci.com//community


Set Up Development Environment
------------------------------

Create a virtual environment and clone this repository::

    $ mkvirtualenv community
    $ git clone git@github.com:elbaschid/pyvr-community.git
    $ cd pyvr-community
    $ setvirtualenvproject

The next thing to do is to install all the requirements for the project. Since
we are setting up the development environment and will require additional
packages for that, we'll use the ``requirements-dev.txt`` requirement file::

    $ pip install -r requirements-dev.txt


Running Django
~~~~~~~~~~~~~~

Create the initial database and apply all migrations::

    $ ./manage.py migrate

This should set up your database(s) assuming that you have docker environment
running. After that, start the server and check out the website in your browser
at http://localhost:8000::

    $ ./manage.py runserver


.. _`docs on new migrations`: https://docs.djangoproject.com/en/dev/topics/migrations/


Running Tests
-------------

For a full test run including *PEP8* checking run *py.test* with the PEP8
plugin::

    $ py.test --pep8

Running the full test suite with PEP8 checking and coverage report, run::

    $ py.test --pep8 --cov  --cov-report html

which will create a ``htmlcov`` directory containing nicely formatted coverage
reports that you can look at in the browser.
