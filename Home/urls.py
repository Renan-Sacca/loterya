from django.urls import path
from django.conf.urls import url, include

from . import views



urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('testePagamento', views.view_that_asks_for_money),
    path('paypal', include('paypal.standard.ipn.urls')),
]