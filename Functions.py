
# Declaration of functions 
def sum(x, y):
    sum  = float(x) + float(y)
    print(sum)

def average(x,y):
    average = (float(x)+float(y)) / 2
    print(average)

def modification(name):
    print(name + "\n Murdoch University")

def PassingListIntoFunction(animals):
    for x in animals :
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