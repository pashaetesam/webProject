from django.shortcuts import render

from Payroll.models import Employee

def EmployeeList(request):
    #Employees=Employee.objects.all()
    Employees=Employee.objects.select_related('EmpDepartment','EmpCountry').all()
    #print(Employees.query)
    TemplateFileName = "Payroll/EmpList.html"
    Dict={"Employees":Employees}
    return render(request,TemplateFileName,Dict)

def EmpDetails(request,id):
    employee= Employee.objects.get(id=id)
    TemplateFileName = "Payroll/EmpDetails.html"
    Dict={"Employee":employee}
    return render(request,TemplateFileName,Dict)
    
    