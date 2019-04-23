import spotipy
import spotipy.util as util
from config import *

def collect_data():
    """
    Collects all the data for your song
    """
    scope = 'user-read-currently-playing'

    token = util.prompt_for_user_token( username,
                                        scope,
                                        client_id = client_id,
                                        client_secret = client_secret,
                                        redirect_uri = redirect_uri)

    sp = spotipy.Spotify(auth=token)
    current_track_info = sp.current_user_playing_track()

    if current_track_info['currently_playing_type'] == 'track':
        current_track_id = current_track_info['item']['id']
        current_track_name = current_track_info['item']['name']

        #see https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-analysis/
        track_analysis = spotify.audio_analysis(current_track_id)
        duration = track_analysis['track']['duration']
        beats = track_analysis['beats']
        bars = track_analysis['bars']
        #finding features like danceability, mood, etc.
        track_features = spotify.audio_features(current_track_id)
        danceability = track_features[0]['danceability']
        loudness = track_features[0]['loudness']
        energy = track_features[0]['energy']
        tempo = track_features[0]['tempo']
        mood = track_features[0]['valence']
    else:
        raise Exception('The audio currently playing is not a track')

    return beats, bars, danceability, loudness, energy, tempo, mood, duration

#beats, bars, danceability, loudness, energy, tempo, mood, duration = collect_data()
#print(beats)
