from django.contrib import admin
from .models import Item, Order, Tax, Discount, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Item)
admin.site.register(Tax)
admin.site.register(Discount)