#Akmal Kurbanov
#Learning Git

print("Time to learn git!")
for i in range(1,11):
    if (i % 2) == 0:
        print(i , "is even")
    else:
        print(i, "is odd")

print("The same task but with lambda and list comprehension")
add = lambda x: print(f"{x} is even") if x % 2 == 0 else print(f"{x} is odd")
[add(i) for i in range(1, 11)]

print("Welcome To GitHub")
class User:
    def __init__(self,name):
        self.name = name
    def print_name(self):
        print(f"My name is {self.name}")

Akmal = User("Akmal")
Akmal.print_name()
    


    
