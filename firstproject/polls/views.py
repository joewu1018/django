from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
# Create your views here.

def hello(request):
	return render(request,"index.html")
def hello1(request,username):
	now=datetime.now()
	return render(request,"index2.html",locals())
def hello2(request,username):
	now=datetime.now()
	return render(request,"index3.html",{"username":"test123","now":now})
	
times = 0

def hello3(request,username):
	now=datetime.now()
	global times
	times = times + 1
	local_times = times
	n1=random.randint(1,6)
	n2=random.randint(1,6)
	n3=random.randint(1,6)
	dict1={"dice1":n1,"dice2":n2,"dice3":n3}
	score=random.randint(1,100)
	return render(request,"index4.html", locals())
	
def students(request):
	std1={"name":"同學1","sid":"000000000","age":18}
	std2={"name":"同學2","sid":"111111111","age":19}
	std3={"name":"同學3","sid":"222222222","age":20}
	stds=[std1,std2,std3]
	return render(request,"std.html",locals())