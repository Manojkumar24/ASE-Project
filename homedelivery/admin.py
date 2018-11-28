from django.contrib import admin
from .models import HD_Address

# Register your models here.
# admin.site.register(HD_FoodOrder)
# admin.site.register(HD_Address)


# class HD_AddressInLine(admin.StackedInline):
#    model = HD_Address


'''class HD_AddressAdmin(admin.ModelAdmin):
    #readonly_fields = ('tokenId',)
    fieldsets = [
        ('TokenID', {'fields': ['tokenId']}),
        #(None, {'fields': ['tokenId']}),
        ('Food Info', {'fields': ['Food_id', 'quantity', 'price']}),
        ('Date Ordered', {'fields': ['date']}),
    ]'''

# inlines = [HD_AddressInLine]


admin.site.register(HD_Address)
<<<<<<< HEAD
=======

>>>>>>> af3034b095dd5c46eb117bf8b54643011e7d093f
