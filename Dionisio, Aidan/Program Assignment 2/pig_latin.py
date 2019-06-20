#pig_latin.py
#Python 3.7.0
#Written by Aidan Dionisio
#September 12, 2018
#Take a given word an convert it to pig Latin.

word = input("Give me a word to convert into Pig Latin: ")
print(word + " in Pig Latin is " + word[1:] + word[:1] +"lay.")
