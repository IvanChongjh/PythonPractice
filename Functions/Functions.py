
# Declaration of functions that takes in two parameters x and y respectively  
def sum(x, y):

    #casting the parameters to float for x and y and store into sum 
    sum  = float(x) + float(y)
    print(sum)
# declaring of functions that takes in two parameters
def average(x,y):
    #casting x and y to float and sum it follow by dividing by two
    average = (float(x)+float(y)) / 2
    print(average)
# declaring a function to take in name 
def modification(name):
    print(name + "\n Murdoch University")

# declaring a function to take in animals 
def PassingListIntoFunction(animals):
    for x in animals : # for each loop through animals and print out all details
     print(x)

#Declaration of Numbers for testing
firstnumber = input("Enter First Number")
secondnumber = input("Enter Second Number")

#Testing Sum Function
sum(firstnumber,secondnumber)

#Testing Average Function
average(firstnumber,secondnumber)

#Testing Modification Function 
name = "Ivan Chong"
modification(name)

#Testing List Passing into function
animals = ["Dog","Cats","Birds"]
PassingListIntoFunction(animals)