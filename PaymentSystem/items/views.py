from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Item, Order, OrderItem
import stripe
from django.conf import settings

def item_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'item.html', context)

def buy_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'unit_amount': int(item.price * 100),
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/').rstrip('/'),
        cancel_url=request.build_absolute_uri('/').rstrip('/'),
    )
    print(request.build_absolute_uri)
    return JsonResponse({'session_id': session.id})

def order_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    context = {
        'order': order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'order.html', context)

def buy_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order_items = OrderItem.objects.filter(order=order)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    line_items = []
    for item in order_items:
        line_item = {
            'price_data': {
                'currency': 'rub',
                'unit_amount': int(item.item.price * 100),
                'product_data': {
                    'name': item.item.name,
                    'description': item.item.description,
                },
            },
            'quantity': item.quantity,
        }
        if order.tax and order.tax.stripe_id:
            line_item['tax_rates'] = [order.tax.stripe_id]
        line_items.append(line_item)

    session_params = {
        'line_items': line_items,
        'mode': 'payment',
        'success_url': request.build_absolute_uri('/').rstrip('/'),
        'cancel_url': request.build_absolute_uri('/').rstrip('/'),
    }

    if order.discount and order.discount.stripe_id:
        session_params['discounts'] = [{'coupon': order.discount.stripe_id}]

    session = stripe.checkout.Session.create(**session_params)
    return JsonResponse({'session_id': session.id})

def index_view(request):
    items = Item.objects.all()
    orders = Order.objects.all()
    return render(request, 'index.html', {
        'items': items,
        'orders': orders,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })