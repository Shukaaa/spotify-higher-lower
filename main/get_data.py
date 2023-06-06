### imports ###
import requests

### Get Endpoint Data ###
def getDataFromEndpoint(ACCESS_TOKEN, ENDPOINT):
    response = requests.get(
        ENDPOINT,
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )
    data = response.json()

    if len(data) == 1:
        print("ERROR: WRONG AUTHKEY")
        return None
    else:
        return data

def playlistBuilder(limit, offset):
    return f"https://api.spotify.com/v1/me/playlists?limit={limit}&offset={offset}"

def getPopularity(data):
    return data['items'][0]['track']['popularity']

def getNameAndArtist(data):
    name = data['items'][0]['track']['name']
    artist = data['items'][0]['track']['album']['artists'][0]['name']

    return f"{name} /// by {artist}"