from django.shortcuts import render

# Create your views here.
def branch_dashboard(request):
    return render(request,'branch_dashboard.html')