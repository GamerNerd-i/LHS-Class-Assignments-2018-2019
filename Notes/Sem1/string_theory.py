#Strings can be opened/closed by either " or '.

print('"Quotes found on the internet are not always accurate." - Abraham Lincoln')

#To bypass quotes/aphostrophes mid-string, use \
#\ indicates to use the secondary function of the next character, such as \n for newline or \t for tab.

print('Porky Pig says, "That\'s all folks!"')
print('"Quotes found on the internet are not always accurate." \n\t- Abraham Lincoln')

#.upper .lower .title change the cases of a given string.
#These can be used to store cases in variables.

name = "ada lovelace"
print(name.upper())
print(name.lower())
print(name.title())
name = name.title()

#Whitespaces can be removed with .strip commands. Whitespace includes spaces, tabs, and newlines. This is also known as "sanitizing."

unsanitary = "        Strip my whitespace daddy         "
print(unsanitary)
print(unsanitary.lstrip())
print(unsanitary.rstrip())
print(unsanitary.strip())
unsanitary = unsanitary.strip()

#You can also add strings together. This is known as "concatenation."
#If the strings don't have whitespace or punctuation in them, it must be added manually as its own string.

weird_quote = name + ": " + unsanitary
print(weird_quote)
