#run-length_encoding.py
#Python 3.7.0
#Written by Aidan Dionisio
#April 29, 2019
#Implement compression and decompression functions for a string.

def encode(s):
    master = ""
    count = 0
    current = 0
    for letter in s:
        if  current < len(s)-1:
            after = s[current+1]
            count += 1
            if letter == after:
                count = count
            else:
                master = master + str(count) + letter
                count = 0
        else:
            count += 1
            master = master + str(count) + letter
        current += 1
    return master

def decode(s):
    master = ""
    runs = len(s)//2
    index = 0
    for char in range(runs):
        letter = s[index + 1]
        for repeater in range(int(s[index])):
            master += letter
        index += 2
    return master
