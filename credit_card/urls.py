from django.conf.urls import url
from credit_card import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^api/credit_card/register_new$', views.register_new_credit_card),
    url(r'^api/credit_card/detail/(?P<number>[0-9]+)$', views.credit_card_detail),
    url(r'^api/credit_card/display_all$', views.all_credit_card),
    url(r'^api/credit_card/register_user$', views.register_user),
    url(r'^api/credit_card/login$', obtain_auth_token),
]
