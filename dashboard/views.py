from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def registerform(request):
    return render(request,'index.html')

def stdashboard(request):
    return render(request,'dashboard/dashboard.html')