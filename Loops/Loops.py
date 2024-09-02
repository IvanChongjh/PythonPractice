i = 10 

print("While Loop Testing\n")
# While Loop 
while i  > 0: #condition if 10 > 0 then -1 
    print(i)
    i-=1

# Creating a list to test for loop

print("for loop Testing \n")
fruits = ["Apple" , "Banana", "Cherry"]

for x in fruits:
    print(x)

# looping through individual characters
for e in "Banana":
    print(e)



print("Testing Continue Statement\n")
# continue statement
# This will loop through list and upon indentifying the names called sarah it will skip and continue to john
names = ["Ivan","Sarah","John"]
for c in names:
    if c == "Sarah":
        continue
    print(c)



print("Testing Nested Loop \n")
# nested loop 

Characters = ["Goblin", "Super", "Zombie"]
Animals = ["Dog","Cat", "Fish", "Bird"]

for p in Characters:
    for u in Animals:
        print(p,u)


