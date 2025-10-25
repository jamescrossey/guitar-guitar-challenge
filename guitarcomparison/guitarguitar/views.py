from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = '38ef8b39fad049f8905aed6f791eddc2',
                                                      client_secret = '02a6251fb74e4b80a8348d1d066f3cd3',
                                                      redirect_uri = 'https://localhost/auth-response',
                                                      ))


def index(request):
    artist1 = request.GET.get('artist1','')
    artist2 = request.GET.get('artist2','')
    artist3 = request.GET.get('artist3','')
    
    if (artist1 or artist2 or artist3):
        artists = [artist1, artist2, artist3]
        for i in range(3):
            if artists[i]:
                genres = []
                genres.append(sp.search(artists[i],type="artist",limit=1))
        context = {'genres' : genres}
        return render(request, 'guitarguitar/comparison.html')


    context = {'artist1' : artist1,
                'artist2' : artist2,
                'artist3' : artist3}
    return render(request, 'guitarguitar/index.html', context)
