from django.shortcuts import render, get_object_or_404
from .models import Item

def item_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {'item' : item}
    return render(request, 'index.html', context)

def buy_view(request):
    pass