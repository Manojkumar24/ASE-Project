from django.contrib import admin
from .models import HD_Address
from .models import HD_Address, HD_FoodOrder
# Register your models here.
# admin.site.register(HD_FoodOrder)
# admin.site.register(HD_Address)



class HD_AddressInLine(admin.StackedInline):
    model = HD_Address


class HD_FoodOrderAdmin(admin.ModelAdmin):
    readonly_fields = ('tokenId',)
    fieldsets = [
        ('TokenID', {'fields': ['tokenId']}),
        #(None, {'fields': ['tokenId']}),
        ('Food Info', {'fields': ['Food_id', 'quantity', 'price']}),
        ('Date Ordered', {'fields': ['date']}),
    ]


admin.site.register(HD_Address,HD_AddressAdmin)
inlines = [HD_AddressInLine]


admin.site.register(HD_FoodOrder, HD_FoodOrderAdmin)

