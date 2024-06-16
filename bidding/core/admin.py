from django.contrib import admin
from .models import Product, Bids

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'starting_bid', 'posted_date', 'ending_date', 'author')
    search_fields = ('product_name', 'author__username')

class BidsAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'amount', 'last_updated')
    search_fields = ('product__product_name', 'user__username')

admin.site.register(Product, ProductAdmin)
admin.site.register(Bids, BidsAdmin)
