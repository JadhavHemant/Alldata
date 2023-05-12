from django.contrib import admin
from RestApp.models import CustomerModel,StateModel,CityModel
# Register your models here.
admin.site.register(CustomerModel)
admin.site.register(StateModel)
admin.site.register(CityModel)

