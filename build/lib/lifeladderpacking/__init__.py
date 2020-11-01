import os
from flask import Flask, request, render_template, Markup
from functools import reduce
from datetime import datetime
from lifeladderpacking.lifeladderApp import ladderLogic
from lifeladderpacking.UI import palletsInShipmentAsOneString
from lifeladderpacking.AppData import maxPackingHeight

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

        try:
            global maxPackingHeight
            maxPackingHeight = int(float(request.args.get('newMaxHeight'))*1000)
        except: 
            pass

        maxHeight = maxPackingHeight/1000

        allOrders = []
        try:
            order1 = [int(request.args.get('amount1')), int(float(request.args.get('length1'))*1000)]
            lights1 = (request.args.get('lights1') == 'on') ; 1, 0
            order1.append(lights1)
            allOrders.append(order1)
        except:
            pass

        try:
            order2 = [int(request.args.get('amount2')), int(float(request.args.get('length2'))*1000)]
            lights2 = (request.args.get('lights2') == 'on') ; 1, 0
            order2.append(lights2)
            allOrders.append(order2)
        except:
            pass

        try:
            order3 = [int(request.args.get('amount3')), int(float(request.args.get('length3'))*1000)]
            lights3 = (request.args.get('lights3') == 'on') ; 1, 0
            order3.append(lights3)
            allOrders.append(order3)
        except:
            pass

        try:
            order4 = [int(request.args.get('amount4')), int(float(request.args.get('length4'))*1000)]
            lights4 = (request.args.get('lights4') == 'on') ; 1, 0
            order4.append(lights4)
            allOrders.append(order4)
        except:
            pass

        try:
            order5 = [int(request.args.get('amount5')), int(float(request.args.get('length5'))*1000)]
            lights5 = (request.args.get('lights5') == 'on') ; 1, 0
            order5.append(lights5)
            allOrders.append(order5)
        except:
            pass

        try: 
            myShipment = ladderLogic(allOrders)
            palletsString = palletsInShipmentAsOneString(myShipment)
            palletsString = Markup(palletsString.replace('\n', '<br>'))
        except:
            return render_template("/index.html") 

        return render_template('pack.html', **locals())

    return app