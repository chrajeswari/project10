from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':1000,'b':2900,'c':300}
    return render(request,'condition.html',d)