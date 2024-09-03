
mytuple = ("ivan","sarah","jimmy","john")

print(mytuple[1])

# tuples are immutable meaning you cannot change the values, hence if you want to change the value you need to put the data into a list and back to tuple

x = list(mytuple) # passing tuple data to cast with list

x[1] = "james"  # change index 1 from sarah to james

y = tuple(x) # cast list back to tuple
 
print(y[1]) # print value of tuple in index 1 
