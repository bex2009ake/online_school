from django.urls import path
from payment.views import *

urlpatterns = [
    path('payment/', Pay.as_view(), name='pay')
]