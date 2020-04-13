from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('postlogin/',views.postlogin),
    path('prephd',views.prephd,name='prephd'),
    path('resmtd',views.resmtd,name='resmtd'),
    path('rrm',views.rrm,name='rrm'),
    path('collaq',views.collaq,name='collaq'),
    path('revsubmit',views.revsubmit,name='revsubmit'),
    path('plagarism',views.plagarism,name="plagarism"),
    path('thesisSubmit',views.theSubmit,name="theSubmit"),
    path('vivavoca',views.vivavoca,name="vivavoca"),
    path('extend',views.extend,name='extend'),
    path('changeSuper',views.changeSuper,name='changeSuper'),

]