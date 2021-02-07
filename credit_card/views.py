from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from credit_card.models import CreditCard
from credit_card.serializers import CreditCardSerializer, RegisterSerializer
from rest_framework.decorators import api_view
from credit_card.functions import validate_date, validate_holder, validate_number, validate_cvv

#registrar novo usuário
@api_view(['POST'])
def register_user(request):
    if request.method == "POST":
        user_data = JSONParser().parse(request)
        user_serializer = RegisterSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            try:
                user = User.objects.create_user(user_data['username'], user_data['email'], user_data['password'])
                Token.objects.create(user=user)
                return JsonResponse(user_serializer.data, status=status.HTTP_200_OK, safe=False)
            except:
                return JsonResponse(user_serializer.data, status=status.HTTP_400_BAD_REQUEST, safe=False)

#registrar novo cartão de crédito
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def register_new_credit_card(request):
    if request.method == 'POST':
        credit_card_data = JSONParser().parse(request)
        try:
            if validate_date(credit_card_data['exp_date'])[0] == True and validate_holder(credit_card_data['holder']) == True and validate_number(credit_card_data['number'])[0] == True and validate_cvv(credit_card_data['cvv']) == True:
                credit_card_data['exp_date'] = validate_date(credit_card_data['exp_date'])[1] #substitui pela data no formato correto
                credit_card_data['brand'] = validate_number(credit_card_data['number'])[1] #adiciona a brand do cartão
                credit_card_serializer = CreditCardSerializer(data=credit_card_data)
                if credit_card_serializer.is_valid(raise_exception=True):
                    credit_card_serializer.save()
                    return JsonResponse(credit_card_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(credit_card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({'mensagem': 'Invalid Parameters'}, status=status.HTTP_400_BAD_REQUEST)

#obter detalhes de um único cartão de crédito
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def credit_card_detail(request, number):
        try:
            if request.method == 'GET':
                credit_card_data = CreditCard.objects.get(number=number)
                credit_card_serializer = CreditCardSerializer(credit_card_data)
                return JsonResponse(credit_card_serializer.data, status=status.HTTP_200_OK)
        except CreditCard.DoesNotExist:
            return JsonResponse({'message': 'Credit card not found!'}, status=status.HTTP_404_NOT_FOUND)

#obter detalhes de todos os cartões de crédito
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def all_credit_card(request):
    if request.method == 'GET':
        credit_card_data = CreditCard.objects.all()
        credit_card_serializer = CreditCardSerializer(credit_card_data, many=True)
        return JsonResponse(credit_card_serializer.data, status=status.HTTP_200_OK, safe=False)
