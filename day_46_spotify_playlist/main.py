import requests
from pprint import pprint
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
URL = "https://www.billboard.com/charts/hot-100/"

# 1. GET ALL THE SONGS
response = requests.get(url=URL)
billboard = response.text
soup = BeautifulSoup(markup=billboard, features="html.parser")
titles_tag = soup.select("li ul li h3")

songs_name = [title.get_text().strip() for title in titles_tag]
print(songs_name)

# 2. SPOTIFY REQUEST
sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            scope="playlist-modify-private",
            show_dialog=True,
            redirect_uri="https://open.spotify.com/",
            cache_path="token.txt"
        )
    )

user_id = sp.current_user()["id"]
pprint(user_id)

songs_uri = []
for song in songs_name:
    result = sp.search(q=f"track:{song} year:2025", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

pprint(songs_uri)

# Create Playlist
playlist_name = "Billboard November"

playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

print("APRES AVOIR CREE LA PLAYLIST")
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uri)
print(f"Playlist '{playlist_name}' created successfully!")

pprint(playlist)
