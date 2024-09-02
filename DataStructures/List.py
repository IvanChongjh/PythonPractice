# In Python there is no Array, We use List instead

# declaration of list 
name = ["Ivan", "Dexter","Sarah","Johnson"]
# this will print the values of list at index 0 
print(name[0])
# this will print only name[0],name[1],name[2] // then number 3 is limit
print(name[0:3])


# if you need to check the number of students in the list 
numberofstudents =  len(name)
print(numberofstudents) 

# if you needd to add an element to list you need to use .append
name.append("Johnny")

print(name)
# notice johnny will be included at the end of the list


# First Method to remove item .POP is to remove items from list 
name.pop(1) 
print(name)

# notice dexter has been removed from list 
#Second Method
name.remove("Ivan") # this will only remove the first ivan as if there are two ivan in the list 
print(name)


# adding list to to a list 

alphb = list ("Hello World")
print(alphb)

#Combining list 

listofname = ("Ivan","Sarah","John")
print(listofname)
listofpet =("Dog","Cats","Monkey")
combinelist = listofname + listofpet
print(combinelist)