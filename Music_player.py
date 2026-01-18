Playlist = []
History = []

def add_song(song_title, song_year):
    Playlist.append([song_title, song_year])
    print(f"Added {song_title}, {song_year} to the queue")
    return None



def play_next():
    if len(Playlist) == 0:
        print("No songs in queue.")
    else:
        History.append(Playlist.pop(0))
        print(f"Now playing: {History[-1][0]}")
    return None

def view_song_year():
    if len(History) == 0:
        print("No song is playing.")
    else:
        print(f"Song was released in {History[-1][1]}")
    return None

def play_previous():
    if len(History) == 0:
        print("No history available.")
    else:
        Playlist.insert(0, History.pop(-1))
        print(f"Rewinding to: {Playlist[0][0]}")
    return None

def view_status():
    print("Playlist: ")
    for song in Playlist:
        print(song)
    print("History: ")
    for song in History:
        print(song)  
    return None

def main():
    while True: 
        print("Music player main menu:")
        print("To add a song to the playlist, select 1")
        print("To play the next song, select 2")
        print("To view the song's release year, select 3")
        print("To play the previous song, select 4")
        print("To view status, select 5")
        print("To exit, select 0")
        choice = input("Select option: ")
        if choice == "1":
                song_name = input("Please enter song name: ")
                song_year = input("Please enter the song's release year: ")
                add_song(song_name, song_year)
        elif choice == "2":
                play_next()
        elif choice == "3":
                view_song_year()
        elif choice == "4":
                play_previous()
        elif choice == "5":
                view_status()
        elif choice == "0":
            print("Closing music player")
            break
        else:
            print("Invalid command")

main()

#add_song("song", 2003)
#add_song("bam", 1000)
#print("Playlist: ",Playlist)
#play_next()
#print("History: ",History)
#view_song_year()
#play_next()
#print("History: ",History)
#view_song_year()
#play_next()
#print("History: ",History)
#view_song_year()
#print("Playlist: ",Playlist)
#print("History: ",History)
#view_status()
#play_previous()
#print("Playlist: ",Playlist)
#print("History: ",History)
#play_previous()
#print("Playlist: ",Playlist)
#print("History: ",History)
#play_next()
#print("Playlist: ",Playlist)
#print("History: ",History)
#view_status()
#print(Playlist[0][0])
