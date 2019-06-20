#Functions are like variables that contain entire blocks of code.
#Built-in functions include print(), random.randint(), and list().
#Functions always end with () to differentiate them from variables.

#Custom functions must be def'd first.
#Defining a function is the equivalent of storing a value in a variable.
#The variables within the parentheses define what data is required for a function to
##work. These are called perameters.
#All perameters must have values passed to them for the function to work.

def describe_pet(animal_type, pet_name):
    print("I have a(n) " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#When you call a function, it performs its coded action.
#The perameters are placed into the parentheses, just like the other functions.

describe_pet("dog", "Fido")
describe_pet("cat", "Scruffles")

#There are many ways to call functions.

print("Example: Printing using a dictionary and nested loops.\n")

pets = {"dog": ["fido", "poochy"],
        "cat": ["scruffles", "mittens", "snowball"]}

print("Let me tell you about my pets.")
for animal in pets.keys():
    for name in pets[animal]:
        describe_pet(animal, name)
