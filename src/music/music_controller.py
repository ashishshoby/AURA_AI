import keyboard
import subprocess
import keyboard
import subprocess
import urllib.parse
import webbrowser
import os



def open_spotify():

    try:

        subprocess.Popen(
            "spotify.exe"
        )

        return "Opening Spotify."

    except:

        return "Could not open Spotify."
    
def search_song(song):

    query = urllib.parse.quote(song)

    os.startfile(
        f"spotify:search:{query}"
    )

    return f"Searching Spotify for {song}"
    
def play_music():

    keyboard.send(
        "play/pause media"
    )

    return "Playing music."

def pause_music():

    keyboard.send(
        "play/pause media"
    )

    return "Toggled playback."


def next_song():

    keyboard.send(
        "next track"
    )

    return "Skipping song."


def previous_song():

    keyboard.send(
        "previous track"
    )

    return "Playing previous song."

def play_song(song):

    query = urllib.parse.quote(song)

    webbrowser.open(
        f"spotify:search:{query}"
    )

    return (
        f"Searching Spotify for {song}"
    )