from flask import Flask, request
from datetime import datetime
from lifeladderApp import ladderLogic
from UI import palletsInShipmentAsOneString
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html><body>
            <h2>Welcome to the LifeLadderPacker</h2>
            <form action="/pack">
                How many LifeLadders? <input type='text' name='amount'>
                <br><br>
                Length? <select name="length"><option value="" class="placeholder" disabled  selected='selected'></option>
                    <option value="1.5" >1.5</option><option value="1.8" >1.8</option><option value="2.1" >2.1</option><option value="2.4" >2.4</option>
                    <option value="2.7" >2.7</option><option value="3.0" >3.0</option><option value="3.3" >3.3</option><option value="3.6" >3.6</option>
                    <option value="3.9" >3.9</option><option value="4.2" >4.2</option><option value="4.5" >4.5</option><option value="4.8" >4.8</option>
                    <option value="5.1" >5.1</option><option value="5.4" >5.4</option><option value="5.7" >5.7</option><option value="6.0" >6.0</option>
                    <option value="6.3" >6.3</option><option value="6.6" >6.6</option><option value="6.9" >6.9</option><option value="7.2" >7.2</option>
                    <option value="7.5" >7.5</option><option value="7.8" >7.8</option><option value="8.1" >8.1</option><option value="8.4" >8.4</option>
                    <option value="8.7" >8.7</option><option value="9.0" >9.0</option></select> meters
                <br><br>
                Include LightUnits? <input type='checkbox' name='lights'>
                <br><br>
                <input type='submit' value='Continue'>
            </form>
        </body></html>
        """

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

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
