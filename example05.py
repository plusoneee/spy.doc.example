from lib.loads import spotify_auth
sp = spotify_auth()
theblackskirt = 'spotify:artist:6WeDO4GynFmK4OxwkBzMW8'
results = sp.artist_related_artists(theblackskirt)
for artist in results['artists']:
    print("| * Name:", artist['name'])
    print("| * Artist ID :", artist['id'])
    print("| * External url:", artist['external_urls']['spotify'])
    print("| * Followers number:", artist['followers']["total"])
    print("| * Genres:", artist['genres'])
    print("| * Popularity:", artist['popularity'])
    print("| * Image Info:")
    for img in artist['images']:
        print("| * url:", img['url'])
        print("| * height:", img['height'])
        print("| * width:", img['width'])
    print('||')