hello-flask
======================================================================

Let's try to deploy this 'Hello, World!' flask application to Heroku!

.. code:: sh

    $ heroku login
    $ heroku apps:create hello-flask-drmc
    $ heroku config:set FLASK_APP=hello.py -a hello-flask-drmc
    $ git push heroku master


It worked!

* https://hello-flask-drmc.herokuapp.com/hello
