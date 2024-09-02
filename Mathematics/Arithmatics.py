
import math # loads math module 



# using math module 
# you can use round() to round to the nearerst whole number 
# example 
pi = math.pi 
rounding = round(pi)
print("The Rounded number from pi is : ",rounding) # notice it rounds to whole number

# if you want to keep to specific decimal number 
testingnumber = 3.12345 # var
testnumber = round(testingnumber,1)
testingnumbertwo = round(testingnumber,2)

print("The Number Rounded to 1 decimal place is : ", testnumber)
print("The Number Round to 2 decimal place is : ", testingnumbertwo)

# if you enter a negative number it will round the left of the decimal place 
testingnum = 32.132
rndnum = round(testingnum,-1)


print("The Number rounded to the 10's place is : ",rndnum)


# declaration of variables
numberOne = 5
numberTwo = 10

# 1 sum 
sum = numberOne + numberTwo
# 2 subtraction
difference = numberOne - numberTwo
# 3 multiplication
multiply = numberOne * numberTwo
# 4 division 
division = numberOne/numberTwo
# 5 modulus  returns remainder after division 
modulus = numberOne%numberTwo



# 1 The Sum is 
print("Sum is : ", sum)
# 2 Subtraction 
print("Subtraction", difference)
# 3 multiplication 
print("Multiplication", multiply)
# 4 division 
print("Division", division)
# 5 modulus
print("Modulus", modulus)