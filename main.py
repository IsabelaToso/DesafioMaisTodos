from app import app
from db_config import mysql
from flask import request
from function import validate_date, validate_holder, validate_number, validate_cvv, encrypt_decrypt

@app.route('/RegisterNewCreditCard', methods=['POST'])
def index():
        _json = request.json
        _exp_date = _json[0]['exp_date']
        _holder = _json[0]['holder']
        _number = _json[0]['number']
        _cvv = _json[0]['cvv']


        if validate_date(_exp_date)[0] == True and validate_holder(_holder) == True and validate_number(_number) == True and validate_cvv(_cvv) == True:
           fullDate = validate_date(_exp_date)[1]
           encryptedNumber = encrypt_decrypt(_number)

           sql = "INSERT INTO creditcard (exp_date, holder, number, cvv) VALUES (%s, %s, %s, %s);"
           data = (fullDate , _holder, encryptedNumber, _cvv)

           conn = mysql.connect()
           myCursor = conn.cursor()
           myCursor.execute(sql, data)
           conn.commit()
           conn.close()

        return 'Credit card successfully registered!'

if __name__ == "__main__":
    app.run(debug=True) #changes immediately reflected in the browser
