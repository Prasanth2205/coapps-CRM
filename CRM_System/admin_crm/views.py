from django.shortcuts import render

# Create your views here.

# def home(request):
#     return render(request,'home.html')

# def login(request):
#     return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')

