from django.shortcuts import render
from .models import EmpDetails
from django.contrib import messages
from CRUDoperation.forms import Empforms
#from CRUDoperation.models import EmpDetails

def showEmp(request):
    showall =  EmpDetails.objects.all()
    return render(request,'Index.html',{"data": showall})

def InsertEmp(request):
    if request.method =="POST":
        if request.POST.get('empname') and  request.POST.get('email') and  request.POST.get('occupation') and  request.POST.get('salary'):
            saverecord =EmpDetails()
            saverecord.empname= request.POST.get('empname')
            saverecord.email =  request.POST.get('email')
            saverecord.occupation = request.POST.get('occupation')
            saverecord.salary = request.POST.get('salary')
            saverecord.save()
            messages.success(request,'Employee ' +saverecord.empname+ ' is saved Successfully')
            return render(request,'insert.html')
    else:
            return render(request,'insert.html')

def EditEmp(request,id):
    editObj = EmpDetails.objects.get(id=id)
    return render(request,'edit.html',{"EmpDetails":editObj})

def UpdateEmp(request,id):
    upEmp = EmpDetails.objects.get(id=id)
    form = Empforms(request.POST,instance=upEmp)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Updated Successfully')
        return render(request,'edit.html',{"EmpDetails":upEmp})

def Delemp(request,id):
    delemp =EmpDetails.objects.get(id=id)
    delemp.delete()
    show = EmpDetails.objects.all()
    return render(request,"Index.html",{"data":show})