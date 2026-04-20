from django.urls import path
from .views import item_view, buy_view

urlpatterns = [
    path('item/<int:pk>', item_view, name='item'),
    path('buy/<int:pk>', buy_view, name='buy')
]
