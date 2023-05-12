from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from RestApp.models import CustomerModel,CompanyModel,StateModel,CityModel

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerModel
        fields=("id","CustomerName","emailAddress")

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model=CompanyModel
        fields=("id","companyName","totalEmployees","address","emailAddress")


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=StateModel
        fields=("id","stateName","stateCode","cities")

class CitySerializer(serializers.ModelSerializer):
    state=PrimaryKeyRelatedField(queryset=StateModel.objects.all(),many=False)
    class Meta:
        model=CityModel
        fields=("id","cityName","cityCode")
