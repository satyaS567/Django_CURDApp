from django.shortcuts import render,redirect
from.models import Employee
# Create your views here.
def index(request):
    employee = Employee.objects.all()

    context = {
        'emp':employee
    }
    return render(request,'index.html',context)

def create(request):
    if request.method =='POST':
        name=request.POST['name']
        department=request.POST['department']
        desgination=request.POST['desgination']
        email=request.POST['email']
        phone=request.POST['phone']
        dateofjoin=request.POST['dateofjoin']
        new_emp=Employee(name=name,department=department,desgination=desgination,email=email,phone=phone,dateofjoin=dateofjoin)
        new_emp.save()
        return redirect("/")
    return render(request,'create.html')

def update(request,id):
    employee = Employee.objects.get(id=id)
    if request.method =='POST':
        new_name=request.POST['name']
        new_department=request.POST['department']
        new_desgination=request.POST['desgination']
        new_email=request.POST['email']
        new_phone=request.POST['phone']
        new_dateofjoin=request.POST['dateofjoin']

        employee.name=new_name
        employee.department=new_department
        employee.desgination=new_desgination
        employee.email=new_email
        employee.phone=new_phone
        employee.dateofjoin=new_dateofjoin
        employee.save()
        return redirect("/")
    return render(request,'update.html',context={'emp':employee})

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')
    

def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        employee = Employee.objects.filter(name__contains=query)

        context={
            'emp':employee
        }
        return render(request,'search.html',context)
    return render(request,'search.html')