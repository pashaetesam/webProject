from django.db import models

# Create your models here.

class Department(models.Model):
    DeptName = models.CharField(max_length=30)
    LocationName = models.CharField(max_length=30)
    
    def __str__(self):
        return self.DeptName

class Country(models.Model):
    CountryName = models.CharField(max_length=30)
    
    def __str__(self):
        return self.CountryName

    


class Employee(models.Model):
    
    Countries = [
        ("IND", "INDIA"),
        ("usa", "United States"),
        ("Sth", "RASth"),
        ("ADB", "ABADA"),
        ("Spa", "Spain"),
        ("Au", "Aus")
        ]
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    TitleName=models.CharField(max_length=30)
    HasPassport=models.BooleanField(max_length=30)
    Salary=models.IntegerField()
    Birthday=models.DateField()
    HireDate=models.DateField()
    Notes=models.CharField(max_length=30)
    #Country=models.CharField(max_length=35,choices=Countries,default=None)
    Email=models.EmailField(default="",max_length=50)
    PhoneNumber=models.CharField(max_length=20,default="")
    EmpDepartment=models.ForeignKey(Department,default=0,on_delete=models.PROTECT,related_name="Departmens")
    EmpCountry=models.ForeignKey(Country,default=0,on_delete=models.PROTECT,related_name="Countries")
    
