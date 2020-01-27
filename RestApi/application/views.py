from django.shortcuts import render
from django.http import HttpResponse
from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def home(request):
    return HttpResponse("Hello")


@api_view(['GET','POST','DELETE'])
def ShowEmployee(request):
    if request.method=='GET':
        emp_list=Employee.objects.all()
        seri=EmployeeSerializer(emp_list,many=True)
        return Response(seri.data)

    if request.method=='POST':
        seri=EmployeeSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
        return Response(seri.data,status=status.HTTP_201_CREATES)

    if request.method == 'DELETE':
          data=Employee.objects.all()
          data.delete()
          return render(request,'application/data.html',{'data':data})



def Table(request):
    data=Employee.objects.all()
    return render(request,'application/data.html',{'data':data})
