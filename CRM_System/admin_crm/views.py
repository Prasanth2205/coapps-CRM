from django.shortcuts import render

# Create your views here.

# def home(request):
#     return render(request,'home.html')

# def login(request):
#     return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')

def deals(request):
    return render(request,'deals.html')

def sales(request):
    return render(request,'sales.html')

def branch (request):
    return render(request,'branch.html')

def account(request):
    return render(request,'account.html')

def inventory(request):
    return render(request,'inventory.html')