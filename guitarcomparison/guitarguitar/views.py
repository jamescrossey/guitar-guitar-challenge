from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


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
