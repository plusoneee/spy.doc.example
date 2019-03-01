from lib.loads import spotify_auth
sp = spotify_auth()
features = sp.audio_features(['2lxcamZ05AtDEtCJbtdvFc'])
print(features)