#!/bin/sh
. venv/bin/activate
export FLASK_APP=hello
export FLASK_ENV=development
flask run
