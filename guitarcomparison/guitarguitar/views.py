from django.shortcuts import render
from models import Type, Guitars
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


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
        for i in range(3):
            if artists[i]:
                artist = artists[i]
                artist_genres = sp.search(artist,type="artist",limit=1)["artists"]["items"][0]["genres"]
                print(artist_genres)
                genres.update(artist_genres)
        print(genres)
        context = {'genres' : genres}
        return render(request, 'guitarguitar/comparison.html')


    context = {'artist1' : artist1,
                'artist2' : artist2,
                'artist3' : artist3}
    return render(request, 'guitarguitar/index.html', context)


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