from django.urls import path
from guitarguitar import views

app_name = "guitarguitar"

urlpatterns = [
    path('', views.index, name='index'),
    path('comparison/', views.comparison, name='comparison'),
    path('compareTwoProducts/', views.compareTwo, name='compareTwo')
]
