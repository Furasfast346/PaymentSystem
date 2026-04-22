from django.urls import path
from .views import item_view, buy_item, order_view, buy_order

urlpatterns = [
    path('item/<int:pk>', item_view, name='item'),
    path('buy-item/<int:pk>', buy_item, name='buy'),
    path('order/<int:pk>', order_view, name='buy_order'),
    path('buy-order/<int:pk>', buy_order, name='order')
]
