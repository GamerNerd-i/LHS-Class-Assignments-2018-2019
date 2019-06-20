#while loops are repeatable if statements.
#Once a while loop ends, it goes back to the "while" line and checks
##that condition again.

#while loops require three things: A control variable, a condition, and
##something to modify the control variable.

#Control variables are those that the while loop depends on.
#As long as the control variable remains true, the loop keeps going.
#To avoid infinite loops, make sure you have a statement that modifies
##the control variable that will eventually make the condition false.
#Also ensure that control variables will be true going into the loop,
##otherwise it won't run at all.

counter = 1

while counter <= 10:
    print(counter)
    counter = counter + 1

print("done\n")

#Use while loops when you're unsure how many times the loop is required
##to run, as opposed to a for loop which has a finite repetition cycle.

print("Example: Write a program that asks users for numbers, and adds" +
      "them together unless they enter a negative number.")

sum_ = 0
num = int(input("Please enter a number (negative to stop): "))

while num >= 0:
    sum_ = sum_ + num
    num = int(input("Please enter a number (negative to stop): "))

print("The total of all numbers entered is " + str(sum_))
