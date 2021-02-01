import datetime
import calendar
import cryptography
from creditcard import CreditCard
from cryptography.fernet import Fernet

#validar a exp_date
def validate_date(exp_date):
    month, year = exp_date.split('/')

    valid = True

    #vê se data é válida
    try:
        exp_date = datetime.date(int(year), int(month), calendar.monthrange(int(year), int(month))[-1])
    except ValueError:
        valid = False

    #vê se data é menor do que a data de hoje
    if valid == True and exp_date < datetime.date.today():
        valid = False

    return valid, exp_date

#validar o holder
def validate_holder(holder):
    valid = False

    if len(holder) > 2:
        valid = True

    return valid

#validar o number
def validate_number(number):
    valid = False

    cc = CreditCard(number)

    if cc.is_valid() == True:
        valid = True

    return valid

#validar o cvv
def validate_cvv(cvv):
    valid = False

    if len(cvv) == 0 or 3 <= len(cvv) <= 4:
        valid = True

    return valid

#encriptar/desencriptar number
def encrypt_decrypt(number):
    #gerando a chave
    key = Fernet.generate_key()

    #armazenar essa chave no banco de dados

    #criptografando
    number = number.encode()
    f = Fernet(key)
    encrypted = f.encrypt(number)

    return encrypted
