class Animal:
    def Speak(self):
        return"Animal Speaks"

class Cat(Animal):
    def Speak(self):
        return "Meow"
cat = Cat()

print('\n ------ Cat Class ------')
print('The cat speaks ', cat.Speak(),'\n')

class Armand:
    def walk(self):
        return"walk"

class Benjamin:
    def speak(self):
        return "Speak"
class Gisubizo:
    def courts(self):
        return "court"

# Multiple inheritance
class David(Armand, Benjamin, Gisubizo):
    pass

david = David()

print("\n ---Badman David ability ----")
print("David can", david.walk())
print("David can", david.speak())
print("David can", david.courts())

# multiple level inheritance

class Trent(David):
    def eat(self):
        return "Eat"
    
trent =Trent()

print("\n ---Trent's ability ----")
print("Trent can", trent.walk())
print("Trent can", trent.speak())
print("Trent can", trent.courts())
print("Trent can", trent.eat())


