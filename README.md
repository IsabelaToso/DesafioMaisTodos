# Desafio MaisTodos: API de cadastro de cartões de crédito
Autora: Isabela Gadelha Toso (isabela.toso@gmail.com, www.linkedin.com/in/isabela-toso)

## Motivação e ferramentas
Esta API foi desenvolvida como parte do desafio técnico de python da empresa MaisTodos. Nela, foram utilizadas a linguagem python 3.9.1 e o framework Django 3.1.2 atrelado ao banco de dados relacional MySQL 8.0.23. A escolha do framework se deve a presença de recursos como django rest e django searchable encrypted fields, que facilitaram a solução desse desafio. O banco de dados foi escolhido devido a familiaridade da autora.

## Introdução
O software tem como objetivo realizar operações de cadastro e consulta de dados de cartões de crédito. Três informações são cadastradas no banco: a data de expiração do cartão, o nome do proprietário, o número, a bandeira e o cvv do cartão. A API permite realizar três ações : cadastrar um novo cartão de crédito, obter detalhes sobre um cartão de crédito específico através de seu número, e obter detalhes sobre todos os cartões de crédito cadastrados no banco. O acesso a API é feito através de sistema de autenticação baseado em sessão com token.

## Função cadastrar cartão de crédito
### URL: api/credit_card/register_new
### Método: POST
### Body: 
Os dados passados devem estar no formato:
```
{
    "exp_date": <string>,
    "holder": <string>,
    "number": <string>,
    "cvv": <int>,
}
```
Com as seguintes restrições:
#### exp_date:
  * estar no formato mm/yy (exemplo: 02/2021);
  * ser uma data válida;
  * ser menor da a data atual (o mês atual é válido);
#### holder:
  * campo obrigatório;
  * possuir mais de 2 caracteres;
#### number:
  * ser válido;
  * cartões de crédito com brand inválida serão cadastrados com     valor de brand vazio;
#### cvv:
  * campo não obrigatório;
  * se presente, possuir entre 3 e 4 caracteres;
  * entrada númerico; 

##### Obs: 
  A validade do campo number e a brand do cartão são obtidos através da lib https://github.com/MaisTodos/python-creditcard. Confira essa documentação para maiores informações.
  
  

## Função consultar detalhes de um cartão de crédito
### URL: api/credit_card/detail/```<number>```
### Método: GET
### Retorno:
```
{
    "exp_date": <string>,
    "holder": <string>,
    "number": <string>,
    "cvv": <int>,
    "brand": <string>
}
```



## Função consultar detalhes de todos os cartões de crédito
### URL: api/credit_card/display_all
### Método: GET



## Função registrar novo usuário
### URL: api/credit_card/register_user
### Método: POST
### Body:
Os dados passados devem estar no formato:
```
{
    "username": <string>,
    "email": <string>,
    "password": <string>
}
```
Com as seguintes restrições:
#### username:
  * não pode ser um usuário já cadastrado no sistema;
#### password:
  * não há restrições quanto a senha;
  
  
  
## Função login
### URL: api/credit_card/login
### Método: POST
### Body:
```
{
    "username": <string>,
    "password": <string>
}
```
##### Obs: 
Nesse software, todos os usuários possuem acesso a todas as funcionalidades do sistema. 


## Testes Unitários
### Arquivos de testes:
* credit_card\Tests\tests_endpoints.py
* credit_card\Tests\tests_functions.py
### Comando para executar os testes:
```
pytest
```

## Considerações
Este software é uma versão simplificada de uma API de cadastro de cartões de crédito e primeiro contato da autora com o desenvolvimento de APIs e com o framework Django. Dessa forma, existem diversas melhorias que podem ser feitas, como por exemplo, a inclusão de mais funcionalidades e a melhoria do sistema de autenticação e autorização, com o implantação de restrições as senhas no momento do cadastro e a implantação de um sistema de autorização diferente para cada grupo de usuários. 


## Referências
###### Django REST framework:
* https://bezkoder.com/django-crud-mysql-rest-framework/
* https://www.django-rest-framework.org
###### Django authentication system
* https://studygyaan.com/django/django-rest-framework-tutorial-register-login-logout
* https://docs.djangoproject.com/en/3.1/topics/auth/default/
###### Django searchable encrypted fields: 
* https://pypi.org/project/django-searchable-encrypted-fields/
###### Datatime:
* https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python
###### Calendar module:
* https://www.w3resource.com/python/module/calendar/monthrange.php
###### Pytest: 
* https://djangostars.com/blog/django-pytest-testing/

