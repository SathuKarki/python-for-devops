class goa:
    name="4576704335"
    drink=""
    def party(self):
        print("Lets party")
    def beach(self):
        print("Lets enjoy the beach")

Diya = goa()
Riya = goa()


Diya.name = "Diya"
Riya.name = "Riya"

print(Diya.name)
Diya.drink = "no"
print("Drink:",Diya.drink)
Diya.beach()

print(Riya.name)
Riya.drink = "yes"
print("Drink:",Riya.drink)
Riya.party()