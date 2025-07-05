from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        a = int(request.POST.get('Num1'))
        b = int(request.POST.get('Num2'))
        Op = request.POST.get('Op')
        if Op == 'add':
            result = a+b
        if Op == 'sub':
            result = a-b
        if Op == 'mul':
            result = a*b
        if Op == 'div':
            result = a/b
        return render(request,'home.html',{'result':result})
    return render(request,'home.html')
def hello(request):
    return HttpResponse('HelloWorld')