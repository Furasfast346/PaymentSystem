from django.urls import path
from .views import item_view, buy_item, order_view, buy_order, index_view

urlpatterns = [
    path('item/<int:pk>', item_view, name='item'),
    path('buy-item/<int:pk>', buy_item, name='buy_item'),
    path('order/<int:pk>', order_view, name='order'),
    path('buy-order/<int:pk>', buy_order, name='buy_order'),
    path('', index_view, name='index'),
]
