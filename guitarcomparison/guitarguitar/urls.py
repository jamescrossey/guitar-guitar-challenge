from django.urls import path
from guitarguitar import views

app_name = "guitarguitar"
url_pattersn = [
    path('', views.index, name='index'),
    path("search/", views.SearchResults, name="search_results")

]
