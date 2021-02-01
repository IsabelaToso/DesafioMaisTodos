from app import app
from db_config import mysql
from flask import request

@app.route('/RegisterNewCreditCard', methods=['POST'])
def index():
        _json = request.json
        _exp_date = _json[0]['exp_date']
        _holder = _json[0]['holder']
        _number = _json[0]['number']
        _cvv = _json[0]['cvv']

        sql = "INSERT INTO creditcard (exp_date, holder, number, cvv) VALUES (%s, %s, %s, %s);"
        data = (_exp_date, _holder, _number, _cvv)

        conn = mysql.connect()
        myCursor = conn.cursor()
        myCursor.execute(sql, data)
        conn.commit()
        conn.close()
        
        return 'Credit card successfully registered!'

if __name__ == "__main__":
    app.run(debug=True) #changes immediately reflected in the browser
