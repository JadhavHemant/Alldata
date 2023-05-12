from rest_framework import generics
from RestApp.models import CustomerModel
from RestApp.Serializer import CustomerSerializer
class CustomerView(generics.ListCreateAPIView):
    queryset=CustomerModel.objects.all()
    serializer_class=CustomerSerializer

class CustomerDetail(generics.ListCreateAPIView):
    queryset=CustomerModel.objects.all()
    serializer_class=CustomerSerializer
