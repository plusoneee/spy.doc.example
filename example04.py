from lib.loads import spotify_auth
sp = spotify_auth()
theblackskirt = 'spotify:artist:6WeDO4GynFmK4OxwkBzMW8'
results = sp.artist(theblackskirt)
print("| * Name:", results['name'])
print("| * Artist ID :", results['id'])
print("| * External url:", results['external_urls']['spotify'])
print("| * Followers number:", results['followers']["total"])
print("| * Genres:", results['genres'])
print("| * Popularity:", results['popularity'])
print("| * Image Info:")
for img in results['images']:
    print("| * url:", img['url'])
    print("| * height:", img['height'])
    print("| * width:", img['width'])