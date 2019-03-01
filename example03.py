from lib.loads import spotify_auth
sp = spotify_auth()
playlists = sp.user_playlists('plusoneee')
items = playlists['items'][0]
print('| * Playlists link:', items['external_urls']['spotify'])
print('| * Playlist ID:' ,items['id'])
print('| * User :', items['name'])
print('| * Owner :', items['owner']['display_name'])
print('| * Profile Url:',  items['owner']['external_urls']['spotify'])
print('| * Song Number:', items['tracks']['total'])
print('| * Track:', items['tracks']['href'])
############################################################
results = sp.user_playlist("plusoneee", items['id'])
track = results['tracks']['items']
print('| | * Playlists Detail:')
for song in track[:]:
    print('| | ')
    print('| | * Artists Name: ', song['track']['artists'][0]['name'])
    print('| | * Artists ID: ', song['track']['artists'][0]['id'])
    print('| | * Album Name: ', song['track']['album']['name'])
    print('| | * Album Release Date: ', song['track']['album']['release_date'])