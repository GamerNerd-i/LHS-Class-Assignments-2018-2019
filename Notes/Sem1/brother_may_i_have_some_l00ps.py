#You'll often want to alter every object in a list.

toppings = ["sausage", "pepperoni", "pineapple", "goat cheese", "bacon", "onions"]

#for loops iterate (go through every item in the list) and act
# for <variable> in <list>: = "for each <variable> in the list <list>"
#Consider your code to be for one item.
#Python will execute that code for every item on the list.

print("Example: Use a for: loop to print the list <toppings> declaring that I like that topping.")

for topping in toppings:
    print("I like " + topping + " on my pizza.")

#Anything indented after the loop is considered to be part of the loop.
#Blank lines are ignored when reading loops. Only tabs are read.
#Therefore, anything after the loop that's not indented is performed alone.
#If something seems off with your loops, double check your indents.

print("\nI *really* like pizza.")

#range() generates numbers.

#A single number in parenthesis tells you how many items are in the list.
#Specifically, it'll give you 0 through n-1.
#In this example,0-7 is printed.

print("\nExample: Use range() to print a list up to 7, and each item individually.")

nums = list(range(8))
print(nums)

for num in nums:
    print(num)


#Two numbers in the range function act as the starting and stopping values.
#The stopping value is not included.

print("\nExample: Print range(1,21).")

nums = list(range(1,21))
print(nums)

#Slices access a given section of the list.
#The digits provided are the indices of the desired items.

print("\nExample: Print the items at indices 15 through 20.")

for num in nums[15:20]:
    print(num)

#Leaving sides blank indicate "up to that side."
#Therefore, both sides blank indicate the entire list.

print("\nExample: Print from the start to index 3.")

for num in nums[:3]:
    print(num)

print("\nExample: Print from index 17 to the end.")

for num in nums[17:]:
    print(num)

#A third number in range() tells python how to count.
#Examples include counting by 2s, 5s, 10s, etc.

print("\nExample: Print the multiples of 4 up to 20.")

nums = list(range(0, 21, 4))

for num in nums:
      print(num)

#Another side note: range() can be plugged directly into for: statements as its own list.

print("\nExample: Print all multiples of 2 up to 20.")

for num in range(0, 21, 2):
    print(num)

print("\nExample: Print all the squares of the even numbers up to 20.")

for num in range(0, 21, 2):
    print(num**2)

#DO NOT copy lists like this:
#new_list = old_ list

#Do this instead:
#new_list = old_list[:]
#This takes a slice of the old list, instead of linking the two.    
