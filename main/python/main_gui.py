import PySimpleGUI as sg
from get_data import *

#######################
### AUTH KEY WINDOW ###
#######################

import PySimpleGUI as sg
from main.python.get_data import *

def authProcess():
    layout = [
        [sg.Text("Auth Window")],
        [sg.In(size=(50, 1), enable_events=True, key="-AUTH-")],
        [sg.Text(key="ERROR", text_color="red")],
        [sg.Button("Submit Auth Key")]
    ]

    window = sg.Window(title="Authorize Access Key", layout=layout)

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        
        ### Check if Auth Key is working ###
        if event == "Submit Auth Key":
            if values["-AUTH-"] == "":
                window.Element("ERROR").update(value="Empty Input")
                window.refresh()
            else:
                ACCESS_TOKEN = values["-AUTH-"]
                data_playlist = getDataFromEndpoint(ACCESS_TOKEN, playlistBuilder(0, 0))
                if data_playlist == None:
                    window.Element("ERROR").update(value="Wrong Access Token")
                    window.refresh()
                else:
                    break
                    
    window.close()
    return ACCESS_TOKEN

#######################
### CHOOSE PLAYLIST ###
#######################

def choosePlaylistProcess():
    ACCESS_TOKEN = authProcess()
    data_playlist = getDataFromEndpoint(ACCESS_TOKEN, playlistBuilder(0, 0))

    ### Listing Playlists ###
    layout = [
        [sg.Text("Choose Playlist")]
    ]

    maxCount = 0
    for i in range(0, data_playlist['total']):
        d = getDataFromEndpoint(ACCESS_TOKEN, playlistBuilder(1, i))
        if d['items'][0]['name'] != "":
            if i == 0:
                radio = [sg.Radio(text=d['items'][0]['name'], group_id=1, default=True, key=i)]
            else:
                radio = [sg.Radio(text=d['items'][0]['name'], group_id=1, default=False, key=i)]
            if i == 27:
                break
        layout.append(radio)
        maxCount = i-1
    d = getDataFromEndpoint(ACCESS_TOKEN, playlistBuilder(1, maxCount+2))
    layout.append([sg.Radio(text=d['items'][0]['name'], group_id=1, default=False, key=maxCount+2)])
    layout.append([sg.Button("Submit Playlist")])

    window = sg.Window(title="Choose Playlist", layout=layout)

    while True:
        event, values = window.read()
            
        if event == sg.WIN_CLOSED:
            break

        if event == "Submit Playlist":
            for x in values:
                if values[x] == True:
                    playlist_id = x
                    break
            break    
    window.close()
    return [ACCESS_TOKEN, playlist_id]

def main():
    data = choosePlaylistProcess()
    ACCESS_TOKEN = data[0]
    playlist_id = data[1]

    playlist_data = getDataFromEndpoint(ACCESS_TOKEN, playlistBuilder(1, playlist_id))
    print(f"You choose: {playlist_data['items'][0]['name']}")

### Start ###
if __name__ == '__main__':
    main()