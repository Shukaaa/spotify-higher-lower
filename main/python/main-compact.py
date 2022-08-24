### imports ###
from random import randint
import requests


####################
### Data Section ###
####################


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

# Playlist Link Shorthand
def playlistBuilder(limit, offset):
    return f"https://api.spotify.com/v1/me/playlists?limit={limit}&offset={offset}"

# Get Popularity Shorthand
def getPopularity(data):
    return data['items'][0]['track']['popularity']

# Get Track and Artist String
def getNameAndArtist(data):
    name = data['items'][0]['track']['name']
    artist = data['items'][0]['track']['album']['artists'][0]['name']

    return f"{name} /// by {artist}"


####################
### Game Section ###
####################


# LooseMSG
def looseMSG(score):
    print(f"""
    You loose :(
    Your score was: {score}
    """)

# WinMSG & Count Score Up
def winMSG(score):
    print("You're right +1")
    return score + 1

# Game Start
def startGame(ACCESS_TOKEN, playlist_data):
    playlist = getDataFromEndpoint(ACCESS_TOKEN, f"{playlist_data['items'][0]['href']}/tracks?limit=1")

    # Game Loop until loose
    score = 0
    while (1):
        # Generates 2 random ints, retry if they're matching
        while(1):
            random1 = randint(0, playlist['total']-1)
            random2 = randint(0, playlist['total']-1)
            if random1 != random2:
                break
        
        # Get Track-Data from ranInts
        track1 = getDataFromEndpoint(ACCESS_TOKEN, f"{playlist_data['items'][0]['href']}/tracks?limit=1&offset={random1}")
        track2 = getDataFromEndpoint(ACCESS_TOKEN, f"{playlist_data['items'][0]['href']}/tracks?limit=1&offset={random2}")

        # Print Score and Track Name + Artist
        print(f"Score: {score}")
        print(f"""Wich Track is more popular: 
        1. {getNameAndArtist(track1)}
        2. {getNameAndArtist(track2)}
        """)
        
        # Get the guess and check if its greater then the other one
        choice = input("Type 1 or 2: ")
        if choice == "1":
            if getPopularity(track1) >= getPopularity(track2):
                score = winMSG(score)
            else:
                looseMSG(score)
                break
        if choice == "2":
            if getPopularity(track2) >= getPopularity(track1):
                score = winMSG(score)
            else:
                looseMSG(score)
                break


#######################
### Prepare Section ###
#######################


### Main Class ###
def main():
    ### Check if Auth Key is working ###
    while (1):
        ACCESS_TOKEN = input("Enter Access Token: ")
        data_playlist = getDataFromEndpoint(ACCESS_TOKEN, playlistBuilder(0, 0))
        if data_playlist != None:
            break

    ### Listing Playlists ###
    maxCount = 0
    for i in range(0, data_playlist['total']):
        d = getDataFromEndpoint(ACCESS_TOKEN, playlistBuilder(1, i))
        print(f"ID: {i} | {d['items'][0]['name']}")
        maxCount = i

    ### Choose Playlist  ###
    while(1):
        playlist_id = input("Type ID of the Playlist you want to choose: ")

        if playlist_id.isnumeric():
            playlist_id = int(playlist_id)
            if playlist_id >= 0 and playlist_id <= maxCount:
                break
            else:
                print("Number out of count")
        else:
            print("Input not a number")
    
    # Get Data from choosen Playlist
    playlist_data = getDataFromEndpoint(ACCESS_TOKEN, playlistBuilder(1, playlist_id))
    print(f"You choose: {playlist_data['items'][0]['name']}")

    # Game Loop for retry
    while(1):
        startGame(ACCESS_TOKEN, playlist_data)
        retry = input("""
        Do you want to retry?
        Type <r> if you want
        """)
        if retry != "r":
            break


### Start ###
if __name__ == '__main__':
    main()
