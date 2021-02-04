from rest_framework import serializers
from credit_card.models import CreditCard

class CreditCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditCard
        fields = ('id',
                  'exp_date',
                  'holder',
                  'number',
                  'cvv',
                  'brand')
