#!/usr/bin/env python

#  Programa: main.py
# Propósito: Creación aplicación web Flask
#     Autor: Óscar García
#     Fecha: 09/12/2019

import flask
import socket
import redis
import os

REDIS_LOCATION=os.environ["REDIS_LOCATION"]

# Crear el objeto que representa la aplicacion web
APP = flask.Flask(__name__)
redis_cli = redis.Redis(host=REDIS_LOCATION, port=6379, db=0)


@APP.route('/')
def index():
    """ Muestra la página inicial asociada al recurso `/`
        y que estará contenida en el archivo index.html
    """
    userinfo = {
        'username': 'Silviu'
    }
    redis_cli.incr('num_visitas')
    num_visitas = redis_cli.get('num_visitas')
    hostname = socket.gethostname()
    return flask.render_template('index.html',
                                 visit_counter=num_visitas.decode("utf-8"),
                                 user=userinfo,
                                 server_name=hostname)

@APP.route('/reset')
def reset():
    userinfo = {
        'username': 'Silviu'
    }
    redis_cli.set('num_visitas', '0')
    num_visitas = redis_cli.get('num_visitas')
    hostname = socket.gethostname()
    return flask.render_template('index.html',
                                 visit_counter=num_visitas.decode("utf-8"),
                                 user=userinfo,
                                 server_name=hostname)

if __name__ == '__main__':
    APP.debug = True
    APP.run(host='0.0.0.0', port=5000)
