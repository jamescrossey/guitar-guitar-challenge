from django.urls import path
from guitarguitar import views

app_name = "guitarguitar"
url_patterns = [
    path('', views.index, name='index'),
    path("search/", views.SearchResults, name="search_results")

]
