from django.db import models
# Create your models here.
class CustomerModel(models.Model):
    CustomerName=models.CharField(max_length=100)
    emailAddress=models.CharField(max_length=100)

class CompanyModel(models.Model):
    companyName=models.CharField(max_length=100)
    totalEmployees=models.IntegerField()
    address=models.CharField(max_length=100)
    emailAddress=models.CharField(max_length=50)
    

class StateModel(models.Model):
    stateName=models.CharField(max_length=100)
    stateCode=models.CharField(max_length=20)
    class Meta:
        ordering=("stateName",)
    def __str__(self):
        return self.stateName

class CityModel(models.Model):
    cityName=models.CharField(max_length=100)
    cityCode=models.CharField(max_length=20)
    state=models.ForeignKey(StateModel,related_name="cities",on_delete=models.CASCADE)
    class Meta:
        ordering=("cityName",)
    def __str__(self):
        return self.cityName


