from django.urls import path
from guitarguitar import views

app_name = 'guitarguitar'

urlpatterns = [
    path('', views.home, name='home'),
    path('comparison/', views.comparison, name='comparison'),
               ]