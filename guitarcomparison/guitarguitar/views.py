from django.shortcuts import render
from models import Type, Guitars

def home(request):
    context_dict = {}
    return render(request, 'guitarguitar/home.html', context_dict)

def comparison(request):

    products_list = Guitars.Objects.all()
    types_list = Type.objects.all()

    sort_options = {
        'price_asc': 'Cheapest First',
        'price_desc': 'Most Expensive First',
    }
    
    sort_by = request.GET.get('sort', '')
    if sort_by == 'price_asc':
        products_list = products_list.order_by('price')
    elif sort_by == 'price_desc':
        products_list = products_list.order_by('-price')


    selected_in_stock = request.GET.getlist('qtyInStock')
    if selected_in_stock:
        products_list = products_list.filter(qtyInStock__gt=0)


    selected_type = request.GET.get('type')
    if selected_type:
        products_list = products_list.filter(type_id=selected_type)

    
    
    context_dict = {'products' : products_list,
                    'types' : types_list,
                    'sort_options' : sort_options,
                    }
    return render(request, 'guitarguitar/comparison.html', context_dict)
