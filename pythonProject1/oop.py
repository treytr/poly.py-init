class fruits:
    def __init__(self,name,price,colour):
        self.name=name
        self.price=price
        self.colour=colour

    def onyesha(self):
       print(f"my favourite fruit is  {self.name}"
             
             f" and it costs ksh. {self.price}"
             f" "
             f"and its colour is {self.colour}")

myobj=fruits("orange","20","orange")
myobj.onyesha()
myobj=fruits("apple","30","red")
myobj.onyesha()