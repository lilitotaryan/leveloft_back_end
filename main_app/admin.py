from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Address, Apartment, Building, Floor
# Register your models here.

@admin.register(Address)
class AddressAdminModel(ModelAdmin):
    pass

@admin.register(Apartment)
class ApartmentAdminModel(ModelAdmin):
    pass

@admin.register(Building)
class BuildingAdminModel(ModelAdmin):
    pass

@admin.register(Floor)
class FloorAdminModel(ModelAdmin):
    pass