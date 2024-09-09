class Person:
  # declaring default constructor 
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # declaring class methods
  def myfunc(self):
    print("Hello my name is " + self.name)


class Goblin:
  def __init__(self,health,attacktype):
    self.health = health 
    self.attacktype = attacktype
  def GoblinScreams(self):
    print("YAWHHHAAAAHHAHAA Tasty")
  def AttackOnZombie(self, damage):
    self.health = self.health - damage
    print("New Zombie Health is " + str(self.health) + "\n Damage Took :" + str(damage) )


 # codes starts here 
p1 = Person("John", 36)
p1.myfunc() 

g1 = Goblin(150,"range")
g1.AttackOnZombie(15)
g1.GoblinScreams()
