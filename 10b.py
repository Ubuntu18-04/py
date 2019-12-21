class bill:
    def __init__(self,cname,name):
        self.cname=cname
        self.name=name
        self.rate=int(input("Enter the amount: "))
        self.quantity=int(input("Enter the quantity:"))
        self.itemTotal=self.rate*self.quantity
        
    def display(self):
        print("Customer_name\titem_name\trate\tquantity\ttotal\n")
        print(self.cname,"\t",self.name,"\t",self.rate,"\t",self.quantity,"\t",self.itemTotal,"\n")
        
  
cust=[]
n=int(input("Enter number of customers"))
for i in range(n):
    cname=input("Enter customer name: ")
    name=input("Enter item the name: ")
    cust.append(bill(cname,name))

print("-----------")
for i in cust:
    i.display()      