import os
from flask import Flask, request, render_template, Markup

from datetime import datetime
from lifeladderpacking.lifeladderApp import ladderLogic
from lifeladderpacking.UI import palletsInShipmentAsOneString

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def home():
        return render_template("/index.html") 

    @app.route('/pack')
    def pack():
        order1 = [int(request.args.get('amount1')), int(float(request.args.get('length1'))*1000)]
        lights1 = (request.args.get('lights1') == 'on') ; 1, 0
        order1.append(lights1)

        order2 = [int(request.args.get('amount2')), int(float(request.args.get('length2'))*1000)]
        lights2 = (request.args.get('lights2') == 'on') ; 1, 0
        order2.append(lights2)

        allOrders = [order1, order2]
        myShipment = ladderLogic(allOrders)
        palletsString = palletsInShipmentAsOneString(myShipment)
        palletsString = Markup(palletsString.replace('\n', '<br>'))

        return render_template('pack.html', **locals())

    return app