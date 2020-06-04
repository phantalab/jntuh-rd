from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
   
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
    
    path('prephdSubmit/',views.prephdSubmit),
    path('resmtdSubmit/',views.resmtdSubmit),
    path('rrmSubmit/',views.rrmSubmit),
    path('collaqSubmit/',views.collaqSubmit),
    path('revsubmitSubmit/',views.revsubmitSubmit),
    path('plagarismSubmit/',views.plagarismSubmit),
    path('thesisSubmitSubmit/',views.theSubmitSubmit),
    path('vivavocaSubmit/',views.vivavocaSubmit),
    path('extendSubmit/',views.extendSubmit),
    path('changeSuperSubmit/',views.changeSuperSubmit)


]
# path('postlogin/',views.postlogin),