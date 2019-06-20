#Function: Calculate user's age based on year of birth and current year.

print("I am going to calculate your age based on your birth year.")
print()
name = input("What is your name? ")

#print() basically creates a newline.
#Composition of functions works well for efficiency.
#current_year serves as an example.

current_year = int(input("Enter the current year:  "))
birth_year = input("Enter your year of birth: ")

#For input prompts, generally end with a space.

birth_year = int(birth_year)

#Remember that input() returns strings.
#Use int() to convert it into an integer.

age = current_year - birth_year
print(name.title() + " will turn " + str(age) + " year(s) old this year!")

#Likewise, str() converts integers into strings for usage.
