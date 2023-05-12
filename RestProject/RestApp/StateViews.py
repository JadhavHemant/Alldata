from rest_framework import serializers
from RestApp.models import StateModel,CityModel
from RestApp.Serializer import StateSerializer,CitySerializer
from rest_framework.response import Response 
from rest_framework.decorators import APIView

class StateView(APIView):
    def get(self,request,format=None):
        states=StateModel.objects.all()
        serializers=StateSerializer(states,many=True)
        return Response(serializers.data)

class CityView(APIView):
    def get(self,request,format=None):
        cities=CityModel.objects.all()
        serializers=StateSerializer(cities,many=True)
        return Response(serializers.data)