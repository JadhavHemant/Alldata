from django.http.response import JsonResponse
from rest_framework import serializers,status
from django.shortcuts import render
# import rest_framework
from rest_framework.decorators import APIView
from rest_framework.response import Response
from RestApp.models import CompanyModel
from RestApp.Serializer import CompanySerializers
from rest_framework.parsers import JSONParser
# rest_framework.decorators
from rest_framework.decorators import parser_classes

def Page(request):
        return render(request,"Company.html")

class CompanyView(APIView):
    def get(self,request,format=None):
        comapanylist=CompanyModel.objects.all()
        serializers=CompanySerializers(comapanylist,many=True)
        return Response(serializers.data)
    
    # @parser_classes({JSONParser})
    def post(self,request,format=None):
        # print("Inside Post method")
        serializer=CompanySerializers(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailView(APIView):
        def get(self,request,pk,format=None):
            company=CompanyModel.objects.get(pk=pk)
            serializer=CompanySerializers(company)
            return Response(serializer.data)

        def put(self,request,pk,format=None):
            company=CompanyModel.objects.get(pk=pk)
            serializer=CompanySerializers(company,data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

