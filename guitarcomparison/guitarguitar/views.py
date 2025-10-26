from django.shortcuts import render, redirect
from .models import Guitars, matches
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.urls import reverse
from urllib.parse import urlencode


SPOTIPY_CLIENT_ID = '38ef8b39fad049f8905aed6f791eddc2'
SPOTIPY_CLIENT_SECRET = '02a6251fb74e4b80a8348d1d066f3cd3'
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                      client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def index(request):
    artist1 = request.GET.get('artist1','')
    artist2 = request.GET.get('artist2','')
    artist3 = request.GET.get('artist3','')
    
    if (artist1 or artist2 or artist3):
        artists = [artist1, artist2, artist3]
        genres = set()
        for artist in artists:
            if artist:
                artist_genres = sp.search(artist,type="artist",limit=1)["artists"]["items"][0]["genres"]
                genres.update(artist_genres)
        
        query_params = urlencode({'genres': ','.join(genres)})
        comparison_url = f"{reverse('guitarguitar:comparison')}?{query_params}"
        return redirect(comparison_url)
        
    return render(request, 'guitarguitar/index.html')


def comparison(request):

    genres_param = request.GET.get('genres', '')
    genres = [g.strip() for g in genres_param.split(',') if g.strip()]
    if genres:
            matching_types = matches.objects.filter(genre__in=genres).values_list('type', flat=True)

            products_list = Guitars.objects.filter(guitarType__in=matching_types)
    else:
        products_list = Guitars.objects.all()

    colour_map = {
        1:"Red",
        2:"Orange",
        3:"Yellow",
        4:"Green",
        5:"Blue",
        6:"Purple",
        7:"Pink",
        8:"Brown",
        9:"Gold",
        10:"Silver",
        11:"Grey",
        12:"Black",
        13:"White",
        14:"Natural",
        15:"Multicolour"
    }

    body_map = {
        1:"SStyle",
        2:"TStyle",
        3:"DoubleCut",
        4:"OffSet",
        5:"HollowBody",
        6:"VStyle",
        7:"SmallBody",
        8:"Orchestral",
        9:"GrandAuditorium",
        10:"Dreadnought",
        11:"Jumbo",
        12:"Explorer",
        13:"SingleCut",
        14:"Combo",
        15:"Head",
        16:"Cabinet"
    }

    for product in products_list:
        product.colour = colour_map.get(product.colour)
        product.BodyShape = body_map.get(product.BodyShape)

    context_dict = {'products': products_list, 'genres': genres}

    return render(request, 'guitarguitar/comparison.html', context_dict)


def compareTwo(request):
    ids = request.GET.get('ids', '')
    id_list = [i.strip() for i in ids.split(',') if i.strip()]

    guitars = Guitars.objects.filter(sku__in=id_list)


    colour_map = {
        1:"Red",
        2:"Orange",
        3:"Yellow",
        4:"Green",
        5:"Blue",
        6:"Purple",
        7:"Pink",
        8:"Brown",
        9:"Gold",
        10:"Silver",
        11:"Grey",
        12:"Black",
        13:"White",
        14:"Natural",
        15:"Multicolour"
    }

    body_map = {
        1:"SStyle",
        2:"TStyle",
        3:"DoubleCut",
        4:"OffSet",
        5:"HollowBody",
        6:"VStyle",
        7:"SmallBody",
        8:"Orchestral",
        9:"GrandAuditorium",
        10:"Dreadnought",
        11:"Jumbo",
        12:"Explorer",
        13:"SingleCut",
        14:"Combo",
        15:"Head",
        16:"Cabinet"
    }

    for product in guitars:
        product.colour = colour_map.get(product.colour)
        product.BodyShape = body_map.get(product.BodyShape)
    context = {'guitars': guitars}

    return render(request, 'guitarguitar/compare2Products.html', context)


def unused():
    # sort_options = {
    #     'price_asc': 'Cheapest First',
    #     'price_desc': 'Most Expensive First',
    # }
    
    # sort_by = request.GET.get('sort', '')
    # if sort_by == 'price_asc':
    #     products_list = products_list.order_by('price')
    # elif sort_by == 'price_desc':
    #     products_list = products_list.order_by('-price')


    # selected_in_stock = request.GET.getlist('qtyInStock')
    # if selected_in_stock:
    #     products_list = products_list.filter(qtyInStock__gt=0)


    # selected_type = request.GET.get('type')
    # if selected_type:
    #     products_list = products_list.filter(type_id=selected_type)
    return