#Lists are sequences of information, usually in string form.
#Naming convention has lists as plural.

songs = ["Epic Sax Guy", "Never Gonna Give You Up", "Deja Vu"]

#Printing a list returns it like it is in the code.
#It's not really what we want.

print(songs)

#Individual pieces of a list can be accessed by list[index].
#Indeces start at 0. Therefore, an item's index is (position - 1).
#Negative numbers can be used to access the end of the list on, starting at -1.
#For example, both 2 and -1 return "Bohemian Rhapsody."

#Index errors occur when the given index doesn't exist.
#This is common due to the indeces starting at 0.

print(songs[2])
print(songs[-1])

#len() displays how long the list is.

playlist_length = len(songs)
print("There are " + str(playlist_length) + " songs in this list.")

#Lists act exactly like the information they hold.
#Single items can be used as individual strings or integers.

print(songs[1].upper())

#Lists can be modified/manipulated within a program.
#append() adds the item to the end of the list.

print('Example: Append "We Are Number One."')
songs.append("We Are Number One")
print(songs)

#insert() adds the item at a given index.
#This moves the other items up or down to make space for the inserted item.

print('Example: Insert "Shooting Star."')
songs.insert(2, "Shooting Star")
print(songs)

#pop() removes a specific item from the list and stores it for use later.
#Without a given number, it'll remove the last itme.

print('Example: Pop "Deja Vu," then print it alone.')
animeme = songs.pop(-2)
print(songs)
print(animeme)

#del deletes an item permanently. It cannot be recovered.
#Like pop(), an empty del removes the final object in the list.

print('Example: Delete "We Are Number One."')
print(songs)
del songs[-1]
print(songs)

#remove() searches for an item's value, rather than its index, and removes it.

print('Example: Remove "Shooting Star."')
songs.remove("Shooting Star")
print(songs)

#sort() and sorted() both organize a list by alphabetic order, from caps to lowercase first.
#sort() is permanent. sorted() is not.

songs = ["Epic Sax Guy", "Never Gonna Give You Up", "Deja Vu", "Shooting Star", "We Are Number One"]

print("Example: Print 'songs' with sorted(), then print as normal, then sort() and print again.")
print(sorted(songs))
print(songs)
songs.sort()
print(songs)
