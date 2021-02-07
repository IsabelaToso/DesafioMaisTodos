from django.db import models
from encrypted_fields import fields


class CreditCard(models.Model):
    exp_date = models.DateField(auto_now = False, auto_now_add = False)
    holder = models.CharField(max_length=70, blank=False, default="")
    number_data = fields.EncryptedCharField(max_length=255, default="", blank=False)
    number = fields.SearchField(hash_key="f164ec6bd6fbc4aef5647abc15199da0f9badcc1d2127bde2087ae0d794a9a0b", encrypted_field_name="number_data")
    cvv = models.IntegerField(blank=True)
    brand = models.CharField(max_length=70, blank=True, default="")
