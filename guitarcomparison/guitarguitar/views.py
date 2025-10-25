from django.shortcuts import render
fr

def home(request):
    context_dict = {}
    return render(request, 'guitarguitar/home.html', context_dict)
