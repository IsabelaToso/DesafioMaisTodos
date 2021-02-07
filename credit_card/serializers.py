from rest_framework import serializers
from credit_card.models import CreditCard
from django.contrib.auth.models import User
from django.db import models

class CreditCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditCard
        fields = ('id',
                  'exp_date',
                  'holder',
                  'number',
                  'cvv',
                  'brand')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email',
                  'password')
        constraints = [models.UniqueConstraint(fields=['username'], name='unique_username')]
