from django.contrib import admin
from . import models


class DetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'phone')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('type', 'area', 'city', 'pinCode', 'state', 'country')


admin.site.register(models.Product)
admin.site.register(models.ProductDetails)
admin.site.register(models.Details)
admin.site.register(models.Address, AddressAdmin)
