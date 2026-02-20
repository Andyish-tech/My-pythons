class Animal:
    def Speak(self):
        return"Animal Speaks"

class Cat(Animal):
    def Speak(self):
        return "Meow"
cat = Cat()

print('\n ------ Cat Class')
print('The cat speaks ', cat.Speak())