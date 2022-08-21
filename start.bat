@ECHO OFF
TITLE Spotify Games 

SET /P LANG="Choose the Language: (PythonCMD, PythonGUI): "

IF "%LANG%" == "PythonCMD" (
    TITLE Spotify Games / PythonCMD
    ECHO Check if Python is installed:
    python --version
    ECHO Click ANY key when Python is installed
    PAUSE
    python main/python/main.py
)

IF "%LANG%" == "PythonGUI" (
    TITLE Spotify Games / PythonGUI
    ECHO Check if Python is installed:
    python --version
    ECHO Click ANY key when Python is installed
    PAUSE
    ECHO Installing PySimpleGUI Package
    pip install pysimplegui
    ECHO Click ANY key when PySimpleGUI got installed
    PAUSE
    ECHO If error happen try install PySimpleGUI manually
    python main/python/main_gui.py
)