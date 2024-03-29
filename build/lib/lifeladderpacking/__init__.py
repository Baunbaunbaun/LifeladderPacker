import os
from flask import Flask, request, render_template, Markup
from datetime import datetime
from lifeladderApp import ladderLogic
from UI import palletsInShipmentAsOneString

from AppData import maxPackingHeight
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

    # input page
    @app.route('/')
    def home():
        return render_template("/index.html") 

    # output page
    @app.route('/pack')
    def pack():
        maxHeight = maxPackingHeight
        try:
            maxHeight = int(float(request.args.get('newMaxHeight'))*1000)
        except: 
            pass

        allOrders = []

        for index in range(1,6):
            try:
                amount = int(request.args.get('amount'+str(index)))
                length = int(float(request.args.get('length'+str(index)))*1000)
                lights = (request.args.get('lights'+str(index)) == 'on') ; 1, 0
                allOrders.append([amount,length,lights])
            except:
                pass

        try: 
            myShipment = ladderLogic(allOrders, maxHeight)
            palletsString = palletsInShipmentAsOneString(myShipment)
            palletsString = Markup(palletsString.replace('\n', '<br>'))
        except:
            return render_template("/index.html") 

        return render_template('pack.html', **locals())

    return app