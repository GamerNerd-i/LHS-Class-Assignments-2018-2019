#Dictionaries are another data type in Python.
#Similarly to lists, they store sets of data in a variable.
#The difference is that dictionaries assign labels to each piece of data.

mlb_teams = {'Los Angeles': 'Dodgers', "Chicago":"Cubs"}
mlb_teams["Boston"] = "Red Sox"
print(mlb_teams)

#The label (Los Angeles, Boston) is known as a key.
#The data (Dodgers, Red Sox) is known as a value.
#Keys are used to access values from the dictionary.
#Keys can be added without values.
#Values can be almost anything, even lists and dictionaries.

print("The " + mlb_teams["Los Angeles"] + " are playing the " +
      mlb_teams["Boston"] + " in the world series.")

#Unique keys will add them to the dictionary.
#Existing keys will update the value.
#Values can be almost anything, even lists and dictionaries.
#Keys can't be "mutable types" such as lists or dictionaries.

mlb_teams["Los Angeles"] = ["Dodgers" , "Angels"]
print("after Angels")
print(mlb_teams)
print(mlb_teams["Los Angeles"][0])

#Don't actually print dictionaries/lists directly for the final code.
#Definitely do them during debugging.

mlb_teams = {}
finished = False
while not finished:
    city = input("Enter a city (done to quit): ").strip()
    if city == "done":
        finished = True
    else:
        team = input("Enter the MLB team for that city: ")
        mlb_teams[city] = team
        print()

print(mlb_teams)

#The .keys function retreives a list of all the keys in a dictionary.
#It can be used in for statements to print a dictionary's key-value pairs.

for city in mlb_teams.keys():
    print(city.title() + " " + mlb_teams[city].title())
