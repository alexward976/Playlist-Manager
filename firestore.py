# import the firebase_admin package
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('playlist-manager-a733e-firebase-adminsdk-mwz8l-17b784f8ec.json')

# Use credentials to initalize the app.
app = firebase_admin.initialize_app(cred)

# Create a reference to the database.
db = firestore.client()

def print_all_playlists():
    """Prints the ID for each playlist (table) in the database.
    Args: None.
    """

    db = firestore.client()

    playlists = db.collections()

    for playlist in playlists:
        print(playlist.id)

def print_songs_in_playlist(playlist):
    """Prints the ID for each song in a given playlist.
    Args: playlist (string) -- the playlist ID to be used
    """
    
    playlist_ref = db.collection(playlist).get()
    
    for song in playlist_ref:
        print(song.id)

def print_playlist_details(playlist):
    """Prints the song title, artist, and album name for each song in a given playlist.
    Args: playlist (string) -- the playlist ID to be used
    """

    playlist_ref = db.collection(playlist).get()

    for song in playlist_ref:
        print()
        print(f"Song: {song.get("title")}")
        print(f"Artist: {song.get("artist")}")
        print(f"Album: {song.get("album")}")

def delete_song(playlist, song_id):
    """Deletes a song from a given playlist.
    Args: playlist (string) -- the playlist ID to be used
    song_id (string) -- the ID for the song being deleted
    """

    db.collection(playlist).document(song_id).delete()

    print("Song has been deleted from the playlist.")

def add_song(playlist):
    """Adds a song to a given playlist.
    Args: playlist (string) -- the playlist ID to be used
    """

    print(f"Add a song to the {playlist} playlist.")

    song_title = input("Song title: ")
    song_artist = input("Artist: ")
    song_album = input("Album: ")

    new_song = {"title": song_title, "artist": song_artist, "album": song_album}

    # Each song's ID is its title in lowercase
    song_id = song_title.lower()

    db.collection(playlist).document(song_id).set(new_song)

    print("Song was added to the playlist.")

def edit_song(playlist, song_id):
    """Edits a song in a given playlist.
    Args: playlist (string) -- the playlist ID to be used
    song_id (string) -- the ID for the song being edited
    """
    
    song_title = input("Song title: ")
    song_artist = input("Artist: ")
    song_album = input("Album: ")

    updated_song = {"title": song_title, "artist": song_artist, "album": song_album}

    db.collection(playlist).document(song_id).update(updated_song)

    print("Song has been updated.")

# Boolean for the while loop
running = True

while running:

    # Main menu.
    print("What would you like to do?")
    print("1. Create playlist")
    print("2. Add song to a playlist")
    print("3. Edit song in a playlist")
    print("4. Delete song from a playlist")
    print("5. View a playlist")
    print("6. Exit")

    choice = input()

    # Create a playlist.
    if choice == "1":
        print()
        playlist = input("Playlist title: ")
        add_song(playlist)

    # Add a song.
    elif choice == "2":
        print()

        print_all_playlists()

        print("Which playlist would you like to add a song to?")
        print("(Your response must match the playlist name exactly)")
        
        playlist = input()
        add_song(playlist)

    # Edit a song.
    elif choice == "3":
        print()

        print_all_playlists()

        print("Which playlist would you like to edit a song from?")
        print("(Your response must match the playlist name exactly)")

        playlist = input()

        print()
        print_songs_in_playlist(playlist)
        print("Which song would you like to edit? (be sure to type the song name exactly as it appears in the list.)")
        song_id = input()

        edit_song(playlist, song_id)

    # Delete a song.
    elif choice == "4":
        print()

        print_all_playlists()

        print("Which playlist would you like to delete a song from?")
        print("(Your response must match the playlist name exactly)")

        playlist = input()

        print()
        print_songs_in_playlist(playlist)
        print("Which song would you like to delete? (be sure to type the song name exactly as it appears in the list.)")

        song_id = input()

        delete_song(playlist, song_id)

    # View a playlist.
    elif choice == "5": 
        print()

        print_all_playlists()

        print("Which playlist would you like to view?")
        print("(Your response must match the playlist name exactly)")

        playlist = input()

        print_playlist_details(playlist)

    # Exit the program
    elif choice == "6":
        running = False

    print()

        





