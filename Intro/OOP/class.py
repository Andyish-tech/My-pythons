class student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender= gender
    def info(self):
        print(f"My name is {self.name} am aged {self.age} and am {self.gender}")
        
std= student("Andy", 15, "male")
std.info()