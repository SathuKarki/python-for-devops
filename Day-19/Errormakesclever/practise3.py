#create a class called teacher. create variable name and reg no using const
#create func called display which should print the name and reg no of teacher
#create t1 nd t2 obj and pass the name and reg thru obj

class teacher:
    def __init__(self, name, regno):
        self.name=name
        self.regno=regno

t1 = teacher("Geetha","123") #passing parameter thru obj itself
print(t1.name)
print(t1.regno)
