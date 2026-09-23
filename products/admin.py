from django.contrib import admin
from.models import Brand, Category, Product, PriceHistory, Review, Wishlist, PriceAlert

admin.site.register(Brand)
admin.site.register(Category)

class PriceHistoryInline(admin.TabularInline):
    model = PriceHistory
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','brand','category','processor','ram','current_price')
    list_filter = ('brand','category')
    inlines = [PriceHistoryInline]

admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(PriceAlert)