Manage the Python Community in Vancouver
===============================


.. image:: https://travis-ci.com//community.svg
    :target: https://travis-ci.com//community


Set Up Development Environment
------------------------------

Create a virtual environment and clone this repository::

    $ mkvirtualenv community
    $ git clone git@github.com:elbaschid/community.git
    $ cd community
    $ setvirtualenvproject

The next thing to do is to install all the requirements for the project. Since
we are setting up the development environment and will require additional
packages for that, we'll use the ``dev.txt`` requirement file::

    $ pip install -r requirements/dev.txt


Containerized Services
~~~~~~~~~~~~~~~~~~~~~~

First of all, we need to install ``fig`` on the system using the provided
binaries. For Mac OSX run::

    $ curl -L https://github.com/orchardup/fig/releases/download/0.4.2/darwin > /usr/local/bin/fig
    $ chmod +x /usr/local/bin/fig

Or on Linux::

    $ curl -L https://github.com/orchardup/fig/releases/download/0.4.2/linux > /usr/local/bin/fig
    $ chmod +x /usr/local/bin/fig

With docker installed on your system, we start with building the development
boxes that live in a ``docker`` folder of the project. Fig builds all the boxes
by running::

    $ fig build

The full set up of all containers is started similar to vagrant by executing::

    $ fig up

which will build containers (if required), start all of them and attach to 
their output. The containers can be shut down with ``Ctrl + C``. For additional
commands provided by ``fig`` `checkout the fig documentation`_.


.. _`fig`: http://orchardup.github.io/fig/index.html
.. _`vagrant`: http://vagrantup.com/
.. _`docker`: http://docs.docker.com/
.. _`boot2docker`: http://docs.docker.com/installation/mac/
.. _`checkout the fig documentation`: http://orchardup.github.io/fig/cli.html


Django Configuration
~~~~~~~~~~~~~~~~~~~~

This project uses `django-configurations`_ to handle Django settings. It is a
thin wrapper around the ``settings.py`` that modularises the values and makes
it easier to extend and override different settings "profiles". This project
uses the following profiles:


+-----------+-------------------------------------------+-----------------------+
| **Local** | Local development setup.                  | ``settings/local.py`` |
+-----------+-------------------------------------------+-----------------------+
| **CI**    | Used for CI-specific settings.            | ``settings/ci.py``    |
+-----------+-------------------------------------------+-----------------------+
| **Prod**  | Settings for the test/stage/prod servers. | ``settings/prod.py``  |
+-----------+-------------------------------------------+-----------------------+

The configuration profiles are preconfigured in ``conftest.py``, ``manage.py``
and the respective *WSGI* files for the servers. To override the default simply
specify the ``DJANGO_CONFIGURATION`` setting in the shell or provide the
``--configuration`` option to ``manage.py``. These two commands are essentially
the same::

    $ ./manage.py runserver --configuration=CI
    $ DJANGO_CONFIGURATION=CI ./manage.py runserver

Another advantage of *django-configurations* is that it provides an easy way to
overwrite settings when running a command by manipulating environmental
variables. Things such as API keys, the Django secret key and other values
should not be stored in version control but be passed at runtime. To make this
process as simple as possible, we recommend to create a ``environment.sh``
file in the ``www`` directory and export variables there::

    $ echo "export DJANGO_SECRET_KEY='my special secret key'" > environment.sh

You can now source the ``environment.sh`` file once when you activate the
virtual environment and all variables available::

    $ source environment.sh

The file is in the ``.gitignore`` and won't (and shouldn't) be added to the
repository. You could also add the sourcing of the file to you ``postactivate``
script for virtualenvwrapper.


.. _`django-configurations`: http://django-configurations.readthedocs.org/en/latest/


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


Running CI Test
~~~~~~~~~~~~~~~

The full test suite including PEP8 and coverage will be run on `Travis`_ every
time a commit is pushed to github or a pull request is created.
