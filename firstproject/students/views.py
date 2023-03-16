from django.shortcuts import render

# Create your views here.
from students.models import student

def listone(request): 
    try: 
        unit = student.objects.get(stuName="111") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "listone.html", locals())

def listall(request):  
    allStudents = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "listall.html", locals())