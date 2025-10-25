from django.shortcuts import render

def home(request):
    context_dict = {}
    return render(request, 'guitarguitar/home.html', context_dict)

def comparison(request):
    context_dict = {}
    return render(request, 'guitarguitar/comparison.html', context_dict)
