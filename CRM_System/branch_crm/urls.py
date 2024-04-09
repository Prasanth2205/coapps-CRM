from django.urls import path
from . import views

urlpatterns=[
    path('branch_dashboard/', views.branch_dashboard,name='branch_dashboard'),
]