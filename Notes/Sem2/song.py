class Song():
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration # in seconds
        self.play_count = 0
    def __str__(self):
        return ('"' + self.title + '" by ' + self.artist + " (" +
                str(self.duration) + ")")
    def play(self):
        print(str(self) + " is now playing.")
        self.play_count += 1

import random

songs = []

songs.append(Song("The World Revolving", "Toby Fox", 101))
songs.append(Song("Megalovania", "Toby Fox", 156))
songs.append(Song("We Are Number One", "Robbie Rotten", 138))
songs.append(Song("Deja Vu", "Initial D", 265))

print("Here are the songs in my library.")
for song in songs:
    print(str(song))

#If you use standard python names for classes, python will know which
##version to use based on the object's class.

#print()
#songs[0].play()
#songs[1].play()
#print(str(songs[0]) + " has been played " + str(songs[0].play_count) +
##      " time(s).")


print()
print("Let's play them on shuffle!")
for i in range(20):
    song_num = random.randint(0,3)
    songs[song_num].play()

print()
for song in songs:
    print(str(song) + " has been played " + str(song.play_count) +
          " time(s).")
