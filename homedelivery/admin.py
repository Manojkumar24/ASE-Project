from django.contrib import admin
from .models import HD_Address
# Register your models here.
# admin.site.register(HD_FoodOrder)
# admin.site.register(HD_Address)



#class HD_AddressInLine(admin.StackedInline):
#    model = HD_Address


'''class HD_AddressAdmin(admin.ModelAdmin):
    #readonly_fields = ('tokenId',)
    fieldsets = [
        ('TokenID', {'fields': ['tokenId']}),
        #(None, {'fields': ['tokenId']}),
        ('Food Info', {'fields': ['Food_id', 'quantity', 'price']}),
        ('Date Ordered', {'fields': ['date']}),
    ]'''


#inlines = [HD_AddressInLine]


<<<<<<< HEAD
admin.site.register(HD_Address)
=======
admin.site.register(HD_Address)

>>>>>>> 9bf36a9aa4fb910d284e11d1225e627e2774a9b1
