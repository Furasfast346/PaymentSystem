from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Item
import stripe

def item_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {'item' : item}
    return render(request, 'index.html', context)

def buy_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    print(item)
    stripe.api_key = "sk_test_51TOCcq85B5ewcsD1PYWLnx6eaRymu1eLcZ2ScErigptMLqFyyshbPF07q7JLXgjh9i9DhYG8wVMe3wZkijfm4HJg00ey6Pm2yK"
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'unit_amount': int(item.price * 100),  # в копейки!
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/item/' + str(pk),
        cancel_url='http://127.0.0.1:8000/item/'  + str(pk),
    )
    print(session)
    return JsonResponse({'session_id' : session.id})