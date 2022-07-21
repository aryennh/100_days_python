from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
CLIENT_ID = "73d4da45ac4b4419af8faf3d74d062e8"
CLIENT_SECRET = "b3fa4101ab034a0f8776c1f893e35b53"
web_page = "https://web.archive.org/web/20210523115926/https://www.billboard.com/charts/hot-100/2000-08-12/"
response = requests.get(web_page).text
# o_auth = spotipy.oauth2.SpotifyOAuth(CLIENT_ID,CLIENT_SECRET)


soup = BeautifulSoup(response,'html.parser')

top_100 = soup.find_all(name='span',class_='chart-element__information__song text--truncate color--primary')
list = []
for x in top_100:
    name = x.get_text()
    list.append(name)




sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)
spotfi_url = "http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6"
list_of_urls = []
for song in list:
    result = sp.search(q=f"track:{song} year:{2000}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        list_of_urls.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user_id,name="2000-08-12 Billboard 100",public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=list_of_urls)