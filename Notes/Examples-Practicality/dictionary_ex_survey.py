results = {"chocolate": 0,
           "strawberry": 0,
           "vanilla": 0}

choice = ""
print("A) Chocolate\nB) Strawberry\nC) Vanilla\nD) *End survey*\n")
while choice != "D":
    choice = input("Which ice cream flavor do you prefer?").upper()
    print("")
    if choice == "A":
        results["chocolate"] += 1
    elif choice == "B":
        results["strawberry"] += 1
    elif choice == "C":
        results["vanilla"] += 1

print("\nHere are the results!")

for flavor in results.keys():
    print(str(results[flavor]) + " people preferred " + flavor + ".")
