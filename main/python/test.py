import PySimpleGUI as sg


layout = [
    [sg.Text("Choose Playlist")],
    [sg.Radio(text="Test", group_id=1, default=True)]
]

for x in range(0, 4):
    if x == 0:
        radio = [sg.Radio(text=f"Test {x}", group_id=1, default=True)]
    else:
        radio = [sg.Radio(text=f"Test {x}", group_id=1, default=False)]
    layout.append(radio)

print(layout)

window = sg.Window(title="Choose Playlist", layout=layout)

while True:
    event, values = window.read()
        
    if event == sg.WIN_CLOSED:
        break

window.close()