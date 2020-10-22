import os
from flask import Flask, request, render_template

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
        return render_template("/lifeladderpacking/index.html") 

    @app.route('/pack')
    def pack():
        amount = int(request.args.get('amount'))    
        length = float(request.args.get('length'))    
        lights = request.args.get('lights')
        lights = (lights == 'on') ; 1, 0

        order = [[amount, int(length*1000), lights]]
        myShipment = ladderLogic(order)
        palletsString = palletsInShipmentAsOneString(myShipment)
        palletsString = palletsString.replace('\n', '<br>')

        return """
            <html><body>
                You are packing <b>{0}</b> LifeLadders&reg; of length <b>{1}</b> meters<br> 
                LightUnits included? <b>{2}</b><br><br>
                {3}
            </body></html>
            """.format(amount, length, lights, palletsString)

    return app