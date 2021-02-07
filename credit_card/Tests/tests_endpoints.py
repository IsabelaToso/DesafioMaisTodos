from django.test import TestCase
import pytest
import json

@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()

@pytest.mark.django_db(transaction=True)
def test_valid_and_invalid_data(
    api_client
):
    #testando registrar um usuário com request inválido
   url = '/api/credit_card/register_user'
   data = {
       'usename': "Teste",
       'email': "teste.teste@gmail.com",
       'password': "teste12345"
   }
   response = api_client.post(url, content_type='application/json', data=json.dumps(data))
   assert response.status_code == 400

    #testando registrar um usuário válido
   url = '/api/credit_card/register_user'
   data = {
       'username': "Teste",
       'email': "teste.teste@gmail.com",
       'password': "teste12345"
   }
   response = api_client.post(url, content_type='application/json', data=json.dumps(data))
   assert response.status_code == 200

   #testando registrar um usuário com username já existente no banco
   url = '/api/credit_card/register_user'
   data = {
        'username': "Teste",
        'email': "teste.teste@gmail.com",
        'password': "teste12345"
    }
   response = api_client.post(url, content_type='application/json', data=json.dumps(data))
   assert response.status_code == 400

   #testando fazer login com um request inválido
   url = '/api/credit_card/login'
   data = {
        'usename': "TesteInvalido",
        'password': "testeinvalido12345"
   }
   response = api_client.post(url, content_type='application/json', data=json.dumps(data))
   assert response.status_code == 400

   #testando fazer login com um usuário inválido
   url = '/api/credit_card/login'
   data = {
        'username': "TesteInvalido",
        'password': "testeinvalido12345"
   }
   response = api_client.post(url, content_type='application/json', data=json.dumps(data))
   assert response.status_code == 400

   #testando fazer login com um usuário válido
   url = '/api/credit_card/login'
   data = {
        'username': "Teste",
        'password': "teste12345"
   }
   response = api_client.post(url, content_type='application/json', data=json.dumps(data))
   assert response.status_code == 200

   #testando inserir um cartão com request inválido
   url = '/api/credit_card/register_new'
   data = {
        'ext_date': "02/2021",
        'holder': "Teste",
        'number': "4539578763621486",
        'cvv': "123"
   }
   response = api_client.post(url, content_type='application/json', data=json.dumps(data))
   assert response.status_code == 400

   #testando inserir um cartão inválido
   url = '/api/credit_card/register_new'
   data = {
        'exp_date': "02/2021",
        'holder': "Teste",
        'number': "1111111111111111",
        'cvv': "123"
   }
   response = api_client.post(url, content_type='application/json', data=json.dumps(data))
   assert response.status_code == 400

   #testando inserir um cartão válido
   url = '/api/credit_card/register_new'
   data = {
        'exp_date': "02/2021",
        'holder': "Teste",
        'number': "4539578763621486",
        'cvv': "123"
   }
   response = api_client.post(url, content_type='application/json', data=json.dumps(data))
   assert response.status_code == 201

   #testando recuperar um number inválido
   url = '/api/credit_card/detail/1111111111111111'
   response = api_client.get(url)
   assert response.status_code == 404

   #testando recuperar um number válido
   url = '/api/credit_card/detail/4539578763621486'
   response = api_client.get(url, content_type='application/json')
   assert response.status_code == 200

   #testando recuperar todos os cartões de crédito
   url = '/api/credit_card/display_all'
   response = api_client.get(url, content_type='application/json')
   assert response.status_code == 200
