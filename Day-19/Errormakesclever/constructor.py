class laptop:
    def __init__(self):
        self.ram=""
        self.processor="i10"
    def display(self):
        print("ram is",self.ram)
        print("processor is", self.processor)
      

hp=laptop()  
dell=laptop() 
leno=laptop()

hp.ram="8gb"
hp.processor="i5"

dell.ram="16gb"
dell.processor="i7"

leno.ram="24gb"

hp.display()
dell.display()
leno.display()