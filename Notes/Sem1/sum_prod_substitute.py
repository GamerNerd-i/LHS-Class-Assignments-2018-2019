nums = [4, 5, 1, 11, 15, 6]

#sum() adds all the values in the list, but for now we're not allowed to use it.
#Instead, we'll write an algorithm that does the same thing.

sum_ = 0

for num in nums:
    sum_ = num + sum_

#Setting sum_ to 0 allows adding each number without repeats.
#Don't set sum_ = 0 within the loop, otherwise you'll only get the last value.
#This is known as an accumulator. It will work even without lists.
#sum() doesn't work without lists.

#Now, let's write an algorithm to multiply all numbers now.
#It's basically the same.

prod = 1

for num in nums:
    prod = num * prod

#Be careful not to set the prod variable to 0.
#Anything multiplied by 0 = 0 and we don't want that.
