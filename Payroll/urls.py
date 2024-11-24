
from django.urls import path,include

from Payroll import views

app_name = 'Payroll'

urlpatterns=[
path("EmployeeList", views.EmployeeList,name="EmployeeList"),
path("EmpDetails/<int:id>", views.EmpDetails,name="EmpDetails"),
]
