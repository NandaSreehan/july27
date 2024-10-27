from django.shortcuts import render
from django.http import HttpResponse
def prime(request):
    num = request.POST.get('primeNumber')
    a=False
    num=int(num)
    for i in range(2, int((num/2)+1)):
        if (num % i) == 0:
            a=True
            break
    return render(request,'prime.html',{'any':a })