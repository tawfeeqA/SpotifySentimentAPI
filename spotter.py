import sys

import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

from secrets import spotify_user_id, spotify_client_id, spotify_token, spotify_client_secret
import json
import requests
from pprint import pprint
from lyricsgenius import Genius 


genius = Genius("y0EPZDQKZATdA7-jJcjqStKE6sOvfSBp6flqSpSevruF_5Nj7reYYUnMXuo2DPKa")

#fix formatting bokula
# def getauthToken():

def get_playlists(token):
     query = "https://api.spotify.com/v1/users/azl3ds9rq5qzoh88jzs54tyl8/playlists"
     response = requests.get(query,  headers={"Content-Type": "application/json", 
     "Authorization": "Bearer {}".format(token)})
     response_json = response.json()
     pprint(response_json)
     for playlist in response_json["items"]:
            print(playlist["name"], playlist["href"])

def main():
    redirect_uri = "https%3A%2F%2Fgithub.com%2FtawfeeqA"
    scope = "playlist-modify-public, playlist-modify-private, user-library-read, user-top-read"


    playlist_id = "0EMHnvFL7BBIhXVEoEGpSW?si=30b26d07e0654ea3"
    query = "https://api.spotify.com/v1/playlists/{}".format(playlist_id)
   

    response = requests.get(query,  headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format("BQAxSJ6KI97pTA4iVoxKfeVw62FXyz-ltKfLtuqVBnoyF4vmewY0_yG1TKeL9P7bWG8mAA9Xc_ZY5-vTl6tHqQOdapu9xraR4VPEK06njuC_1Z3zdGOcNqbAHNTmd6RMH6Zv7u2NNQsKkCqGxgxBmemt_nocmM36q97cywDFpfFTFuf69Ix7aSIBSmgureg")})

    response_json = response.json()
    pprint(response_json)

    print(response_json['external_urls'])
    print(response_json['name'])

    for i in response_json["tracks"]["items"]:
        song_name = i["track"]["name"]
        artist_lst =  [artist["name"] for artist in i['track']['album']['artists'] ]
        print(song_name,artist_lst)

        for artist in artist_lst:
            lyrics  = genius.search_song(song_name, artist).lyrics
            if lyrics==None:
                continue
            else:
               print(lyrics)

        print("\n")

if __name__== "__main__" :
    #main()
    get_playlists("BQB141e_S20GG2oDW-B8ORI0hPgCyvLy0WAxorfYRdv_p4fVXEQiTuZkYzfCnAGL3QCddUkc_8LL_GWktVHO-oBFqOHRPWvEB0yv4yUPqJoYrkumVbCpsU36YcXGuynN8BSRCzsLL8I0pwZXblWKGymwDyuOIUfPn4FrIpy96hkNroDxY_nAxwjGkRHf8qo")
