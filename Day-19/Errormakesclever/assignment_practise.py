#To create student class and pass vlaues via object to the constructor


class student():
    def __init__(self):
        print("constructor initiated")
        self.name="asdf"
        self.regno="23456"
    def display(self):
        print("Name:",self.name)
        print("RegNo:",self.regno)

s1 = student()  #constrcutor i called wen obj is defined
s2 = student()
s1.name="Tara"
s1.regno="1"

s2.name="varsha"
s2.regno="2"
s1.display()
s2.display()