from django.urls import path
from . import views

# urlpatterns=[
#     path('',views.home,name='home'),
#     path('login',views.login,name='login'),

# ]

urlpatterns=[
    path('dashboard/', views.dashboard,name='dashboard'),
    path('deals',views.deals,name='deals'),
    path('sales',views.sales,name='sales'),
    path('branch',views.branch,name='branch'),
    path('account',views.account, name='account'),
]