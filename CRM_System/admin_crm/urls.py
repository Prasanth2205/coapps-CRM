from django.urls import path
from . import views

# urlpatterns=[
#     path('',views.home,name='home'),
#     path('login',views.login,name='login'),

# ]

urlpatterns=[
    path('dashboard/', views.dashboard,name='dashboard'),
    path('deals',views.deals,name='deals'),
]