from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'myhome.html')
def login(request):
	return render(request,'b.html')
def x(request):
	return render(request,'x.html')