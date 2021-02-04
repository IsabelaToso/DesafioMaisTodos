from django.conf.urls import url
from credit_card import views

urlpatterns = [
    url(r'^api/credit_card/register_new$', views.register_new_credit_card, name= 'register_credit_card'),
    url(r'^api/credit_card/detail/(?P<pk>[0-9]+)$', views.credit_card_detail),
    url(r'^api/credit_card/display_all$', views.all_credit_card),
]
