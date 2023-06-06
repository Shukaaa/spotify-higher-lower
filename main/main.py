# Get auth token here: https://developer.spotify.com

### imports ###
from random import randint
import time
from get_data import *
from console_colors import *
import os

# clear console
clear = lambda: os.system('cls')

####################
### Game Section ###
####################


##### LooseMSG #####
def looseMSG(score):
    print(f"\n{bcolors.FAIL}You're wrong :({bcolors.ENDC} \nYour score was: {score}\n")

def winMSG(score):
    print(f"\n{bcolors.OKGREEN}You're right +1{bcolors.ENDC}\n")
    return score + 1

def startGame(ACCESS_TOKEN, playlist_data):
    playlist = getDataFromEndpoint(ACCESS_TOKEN, f"{playlist_data['items'][0]['href']}/tracks?limit=1")

    score = 0
    while (1):
        while(1):
            random1 = randint(0, playlist['total']-1)
            random2 = randint(0, playlist['total']-1)
            if random1 != random2:
                break
        
        track1 = getDataFromEndpoint(ACCESS_TOKEN, f"{playlist_data['items'][0]['href']}/tracks?limit=1&offset={random1}")
        track2 = getDataFromEndpoint(ACCESS_TOKEN, f"{playlist_data['items'][0]['href']}/tracks?limit=1&offset={random2}")


        print(f"{bcolors.HEADER}Score: {score}{bcolors.ENDC}")
        print(f"""Wich Track is more popular: 
        {bcolors.HEADER}1{bcolors.ENDC}. {getNameAndArtist(track1)}
        {bcolors.HEADER}2{bcolors.ENDC}. {getNameAndArtist(track2)}
        """)
        choice = input(f"Type {bcolors.HEADER}1{bcolors.ENDC} or {bcolors.HEADER}2{bcolors.ENDC}: ")
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
        if d['items'][0]['name'] != "":
            print(f"ID: {i} | {d['items'][0]['name']}")
        maxCount = i-1

    maxCount = maxCount + 1

    while(1):
        ### Choose Playlist  ###
        playlist_id = input("Type ID of the Playlist you want to choose: ")

        if playlist_id.isnumeric():
            playlist_id = int(playlist_id)
            if playlist_id >= 0 and playlist_id <= maxCount:
                break
            else:
                print("Number out of count")
        else:
            print("Input not a number")
    
    
    playlist_data = getDataFromEndpoint(ACCESS_TOKEN, playlistBuilder(1, playlist_id))
    print(f"You choose: {playlist_data['items'][0]['name']}")

    time.sleep(1)
    clear()

    while(1):
        startGame(ACCESS_TOKEN, playlist_data)
        retry = input("Do you want to retry?\nType <r> if you want\n")
        if retry != "r":
            break
        else:
            clear()
    

### Start ###
if __name__ == '__main__':
    main()
