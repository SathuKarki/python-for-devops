#create a class calculator
#create 2 var a and b
#create a func called add, sub, mul, div all func shoudl take 2 var as parameter
#pass values throug obj
class calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def add(self):
        print("addition is",self.a + self.b)

add = calculator(5, 6)
add.add()