#survey_results.py
#Python 3.7.0
#Written by Aidan Dionisio
#October 31, 2018
#Conduct a survey and print its results.

results = {"Pac-Man": 0,
           "Tetris": 0,
           "Donkey Kong": 0,
           "Space Invaders": 0,
           "Centipede": 0,
           "Asteroids": 0}

choice = ""
print("A) Pac-Man \nB) Tetris \nC) Donkey Kong \nD) Space Invaders")
print("E) Centipede \nF) Asteroids \nG) *end survey*")
while choice != "G":
    choice = input("What is your favorite classic arcade game? ").upper()
    print("")
    if choice == "A":
        results["Pac-Man"] += 1
    elif choice == "B":
        results["Tetris"] += 1
    elif choice == "C":
        results["Donkey Kong"] += 1
    elif choice == "D":
        results["Space Invaders"] += 1
    elif choice == "E":
        results["Centipede"] += 1
    elif choice == "F":
        results["Asteroids"] += 1
        
print("\nHere are the results!")

for game in results.keys():
    print(str(results[game]) + " people said " + game + " is their favorite game.")
