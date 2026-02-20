class levelF:
    name="SOD"
l5sod=levelF()

print("name of trade", l5sod.name)


# Calculater

class calculator:
    
    def add(self, a,b):
        return a+b
    def divide(self, a,b):
        if b==0:
            return"Can not divide by zero"
        return a / b 
    
mycal = calculator()
a,b = 10,5

print(f"{a} + {b} = {mycal.add(a,b)}")
print(f"{a} / {b} = {mycal.divide(a,b)}")
