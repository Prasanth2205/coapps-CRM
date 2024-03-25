from django.urls import path
from . import views

# urlpatterns=[
#     path('',views.home,name='home'),
#     path('login',views.login,name='login'),

# ]

urlpatterns=[
    path('dashboard', views.dashboard,name='dashboard'),
<<<<<<< HEAD
    path('deals', views.deals,name='deals'),
=======
>>>>>>> 94a95f4ae637fa5920fce55d75e42aa3adaee0a0
]