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