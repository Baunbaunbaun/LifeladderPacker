from flask import Flask, request
from datetime import datetime
from lifeladderApp import ladderLogic
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html><body>
            <h2>Welcome to the LifeLadderPacker</h2>
            <form action="/greet">
                How many LifeLadders? <input type='text' name='amount'><br><br>
                Length? <input type='text' name='length'><br><br>
                Include LightUnits? <input type='checkbox' name='lights'><br><br>
                <input type='submit' value='Continue'>
            </form>
        </body></html>
        """

@app.route('/greet')
def greet():
    amount = request.args.get('amount')    
    length = request.args.get('length')    
    lights = request.args.get('lights')    
    lights = (lights == 'on') ; 1, 0

    order = [[int(amount), int(length), lights]]
    ladderLogic(order)

    return """
        <html><body>
            <h2>You are packing {0} LifeLadders of length {1} and LightUnits = {2}!</h2>
            
        </body></html>
        """.format(amount, length, lights)

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
