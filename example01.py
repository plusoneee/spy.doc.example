from lib.loads import spotify_auth
sp = spotify_auth()
results = sp.current_user_saved_tracks()
for item in results['items']:
    track = item['track']
    print ('| * ' + track['name'] + ' | ' + track['artists'][0]['name'])
    
