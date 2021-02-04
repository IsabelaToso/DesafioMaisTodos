from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from credit_card.models import CreditCard
from credit_card.serializers import CreditCardSerializer
from rest_framework.decorators import api_view
from credit_card.functions import validate_date, validate_holder, validate_number, validate_cvv

def register_user(request):
    if request.method == "POST":
        form_user = UserCreationForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect('register_credit_card')
    else:
        form_user = UserCreationForm()
    return render(request, 'register.html', {'form_user': form_user})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('register_credit_card')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

@api_view(['GET', 'POST', 'DELETE'])
def register_new_credit_card(request):
    if request.method == 'POST':

            credit_card_data = JSONParser().parse(request)
            validDate, newDate = validate_date(credit_card_data['exp_date'])
            validNumber, brand = validate_number(credit_card_data['number'])
            credit_card_data['exp_date'] = newDate
            credit_card_data['brand'] = brand
            print(credit_card_data['brand'])

            if validDate == True and validate_holder(credit_card_data['holder']) == True and validNumber == True and validate_cvv(credit_card_data['cvv']) == True:
                credit_card_serializer = CreditCardSerializer(data=credit_card_data)
                if credit_card_serializer.is_valid():
                    credit_card_serializer.save()
                    return JsonResponse(credit_card_serializer.data, status=status.HTTP_201_CREATED)
                return JsonResponse(credit_card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def credit_card_detail(request, pk):
    try:
        credit_card_data = CreditCard.objects.get(number=pk)
        if request.method == 'GET':
            credit_card_serializer = CreditCardSerializer(credit_card_data)
            return JsonResponse(credit_card_serializer.data)
    except CreditCard.DoesNotExist:
        return JsonResponse({'message': 'This credit card does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def all_credit_card(request):
    if request.method == 'GET':
        credit_card_data = CreditCard.objects.all()
        credit_card_serializer = CreditCardSerializer(credit_card_data, many=True)
        return JsonResponse(credit_card_serializer.data, safe=False)
