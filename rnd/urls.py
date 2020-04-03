from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('prephd',views.prephd,name='prephd'),
    path('resmtd',views.resmtd,name='resmtd'),
    path('rrm',views.rrm,name='rrm'),
]