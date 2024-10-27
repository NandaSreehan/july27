from django.shortcuts import render
from django.http import HttpResponse

def armstrong(request):
    sum=0
    a=int(request.POST.get('givenNumber'))
    pow=len(str(a))
    for i in range(pow):
        a=int(a/10)
        sum=sum+((a%10)**pow)
    return render(request,'armstrong.html',{'a':sum})