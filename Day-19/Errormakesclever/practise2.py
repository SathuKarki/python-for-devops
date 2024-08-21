#create a class called fruit,. create a variable called color using __init__funct
#crete obj called apple. "pass the color variabe as a parameter thru obj"

class fruit:
    def __init__(self, col):
        self.color=col

apple =fruit("red")  #passing variable thru obj"
print(apple.color)
    