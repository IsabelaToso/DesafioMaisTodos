import pytest
import datetime
import calendar
from credit_card.functions import validate_date, validate_holder, validate_number, validate_cvv

#constantes
valid_date = "02/2021"
invalid_date_format = "02-2026"
invalid_period = "01/2021"
invalid_date = "14/2021"

valid_holder = "Teste"
invalid_holder = "Te"

valid_number = "4539578763621486"
invalid_number = "1111111111111111"
invalid_brand = "00000000000000"

valid_cvv_len_0 = ""
valid_cvv_len_3 = "123"
valid_cvv_len_4 = "1234"
invalid_cvv_len_2 = "12"
invalid_cvv_len_5 = "12345"

#testando função validate_date()
def test_validate_date():
    valid, exp_date = validate_date(valid_date)
    assert valid is True
    assert exp_date == datetime.date(int(2021), int(2), calendar.monthrange(int(2021), int(2))[-1])

    valid, exp_date = validate_date(invalid_date_format)
    assert valid is False
    assert exp_date == '02-2026'

    valid, exp_date = validate_date(invalid_period)
    assert valid is False
    assert exp_date == datetime.date(int(2021), int(1), calendar.monthrange(int(2021), int(1))[-1])

    valid, exp_date = validate_date(invalid_date)
    assert valid is False
    assert exp_date == '14/2021'

#testando função validate_holder()
def test_validate_holder():
    valid = validate_holder(valid_holder)
    assert valid is True

    valid = validate_holder(valid_holder)
    assert valid is True

#testando função validate_number()
def test_validate_number():
    valid, brand = validate_number(valid_number)
    assert valid is True
    assert brand == 'visa'

    valid, brand = validate_number(invalid_number)
    assert valid is False
    assert brand == ''

    valid, brand = validate_number(invalid_brand)
    assert valid is True
    assert brand == ''

#testando função validate_cvv()
def test_validate_cvv():
    valid = validate_cvv(valid_cvv_len_0)
    assert valid is True

    valid = validate_cvv(valid_cvv_len_3)
    assert valid is True

    valid = validate_cvv(valid_cvv_len_4)
    assert valid is True

    valid = validate_cvv(invalid_cvv_len_2)
    assert valid is False

    valid = validate_cvv(invalid_cvv_len_5)
    assert valid is False
