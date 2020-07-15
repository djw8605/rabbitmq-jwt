RabbitMQ JWT
============


Install Dependencies
--------------------

The create-jwt.py script was tested with python 3, but should work with python2 as well.

Create the python3 virtual environment:

    $ python -m venv venv
    $ . venv/bin/activate

Install the dependencies

    $ pip install -r requirements.txt


Keys
----

The private key rabbit-private.pem should be kept secure.


Creating the JWT
----------------

The JWT can be created by running the create-jwt.py script.  By default, the token will be
valid for 12 hours.

    $ ./create-jwt.py

The token is printed to stdout.

