from lib.loads import spotify_auth
sp = spotify_auth()
top_tracks = sp.artist_top_tracks('6WeDO4GynFmK4OxwkBzMW8', country='US')
for item in top_tracks['tracks']:
    print('| * Track Name:', item['name'], ',Track ID:', item['id'])
    print('| * From Album:', item['album']['name'], ', Album ID:', item['album']['id'], 'Release Date:', item['album']['release_date'])
    print('||')