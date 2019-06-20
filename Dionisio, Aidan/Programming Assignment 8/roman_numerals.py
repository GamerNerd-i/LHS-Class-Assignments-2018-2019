#roman_numerals.py
#Python 3.7.0
#Written by Aidan Dionisio
#April 4, 2019
#Take a file and convert Roman numerals to Arabic numerals.

#Conversion tools
converter = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def letter_to_number(letter):
    letter = letter.upper()
    return int(converter[letter])

def numeral_to_number(numeral):
    number = 0
    for letter in numeral:
        current = letter_to_number(letter)
        before = letter_to_number(numeral[numeral.index(letter)-1])
        if int(numeral.index(letter)+1) < len(numeral):
            after = letter_to_number(numeral[numeral.index(letter)+1])
            if  current < after:
                number = number - current
            else:
                number += current
        else:
            number += current
    return number

#Grab files
filein = input("What file would you like to open? ")
fileout = input("In what file would you like to put the results? ")

with open(filein) as inputs:
    numbers = []
    for line in inputs:
        numbers.append(numeral_to_number(line.rstrip()))

with open(fileout, "w") as outputs:
    for number in numbers:
        outputs.write(str(number) + "\n")

inputs.close()
outputs.close()

print("Done!")
