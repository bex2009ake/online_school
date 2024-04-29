from django.urls import path
from home.views import *

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('team/', TeamView.as_view(), name='team'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('website/', WebView.as_view(), name='website'),
    path('webimg/<int:pk>/', WebImgView.as_view(), name='img')
]