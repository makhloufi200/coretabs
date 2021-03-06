from django.contrib import admin
from . import models
# Register your models here.

#admin.site.register(models.Product) # This will add Product to admin site
#admin.site.register(models.Category) # This will add Category to admin site
#admin.site.site_header = "Coretabs Online Shop Administration"
#admin.site.index_title = ""

def make_price_zero(modeladmin, request, queryset):
    queryset.update(price=0)


make_price_zero.short_description = "Make selected products free"

def make_discount(modeladmin, request, queryset):
    for product in queryset:
        product.price = product.price * 80/100
        product.save()


make_discount.short_description = "Make Discount 20%% For products"

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['name']
    list_display = ('name', 'price', 'stock', 'category',)
    list_filter = ('created_at', 'category',)
    actions = [make_price_zero, make_discount]

#admin.site.register(models.Product,ProductAdmin)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('name', 'description',)
    search_fields = ['name']